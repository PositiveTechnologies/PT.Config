# coding=utf8
import os
from baseconfig import Config, MatchingNode


class Lighttpd(Config):
    conftype = 'lighttpd.conf'

    def __init__(self, path, options):
        Config.__init__(self, path, options)
        with open(path, 'r') as f:
            self.config = LighttpdParser(f.read()).parse()
            self._visit()

    def get_opt_offset(self, opt, offset):
        if not isinstance(opt, Array):
            return None
        return opt.offset(offset)

    def _visit(self):
        for i, opt in enumerate(self.config):
            try:
                m = getattr(self, 'visit_{}'.format(opt.__class__.__name__))
                if m:
                    m(opt)
            except AttributeError:
                pass

    def visit_Include(self, opt):
        try:
            if not os.path.isfile(opt.fname):
                fname = os.path.realpath(os.path.join(os.path.dirname(self.source), opt.fname))
            else:
                fname = opt.fname
            with open(fname, 'r') as f:
                data = f.read()
            child_config = LighttpdParser(data).parse()
            self._set_sourcename(child_config, fname)
            return self.config.extend(child_config)
        except OSError:
            print("include path in lineno {} does not exist".format(opt.lineno))

    def _set_sourcename(self, config, fname):
        for stmt in config:
            stmt.source = fname
            if isinstance(stmt, If):
                self._set_sourcename(If.stmts, fname)

    def find_nodes(self, name, context=None):
        ret = []
        for opt in self.config:
            if (context == 'root' and isinstance(opt, If)) or (context == 'if' and not isinstance(opt, If)):
                continue
            ret.extend(self._find(opt, name))
        return ret

    def _find(self, container, name):
        source = None if not hasattr(container, 'source') else container.source

        if isinstance(container, Assignment) and container.left.name == name:
            return [MatchingNode(name, container.right, container.lineno, source=source)]
        elif isinstance(container, Concat) and container.left.name == name:
            return [MatchingNode(name, container.right, container.lineno, source=source)]
        elif isinstance(container, If):
            ret = []
            for opt in container.stmts:
                ret.extend(self._find(opt, name))
            if ret:
                return ret
        return []

    def fill_missing_line(self, option, value, context=None):
        return option + ' = ' + value


class LighttpdParser:
    def __init__(self, data):
        self.lexer = LighttpdLexer(data)
        self.parser = parser

    def parse(self):
        return self.parser.parse()


class LighttpdLexer:
    def __init__(self, data):
        self.lexer = lexer
        self.lexer.input(data)

    def next_token(self):
        token = self.lexer.token()
        return token

import ply.lex as lex
import ply.yacc as yacc

states = (
    ('string', 'exclusive'),
)

ident = r'[a-z][\w-]*'
t_ignore = ' \r\t\f'

tokens = ('NAME', 'ASSIGN', 'NOT_EQUAL', 'EQUAL', 'MERGE', 'OPEN_BRACKET', 'CLOSE_BRACKET', 'BOOLEAN',
          'INTEGER', 'INCLUDE', 'INCLUDE_SHELL', 'VAR', 'DOUBLE_ARROW', 'COMMA', 'OPEN_BRACE', 'CLOSE_BRACE',
          'RE_MATCH',
          'RE_NOT_MATCH', 'PLUS', 'STRING', 'STR')

t_NAME = r'[a-z][\w-]*(\.[a-z][\w-]*)+'
t_ASSIGN = r'='
t_NOT_EQUAL = r'!='
t_EQUAL = r'=='
t_RE_MATCH = r'=~'
t_RE_NOT_MATCH = r'!~'
t_MERGE = r'\+='
t_OPEN_BRACKET = r'\('
t_OPEN_BRACE = r'\{'
t_CLOSE_BRACKET = r'\)'
t_CLOSE_BRACE = r'\}'
t_BOOLEAN = r'"enable"|"disable"'
t_INTEGER = r'[0-9]+'
t_INCLUDE = r'include'
t_INCLUDE_SHELL = r'include_shell'
t_DOUBLE_ARROW = r'=>'
t_COMMA = r','
t_PLUS = r'\+'


def t_error(t):
    t.lexer.skip(1)
    raise Exception("Illegal character '{}'".format(t.value[0]))


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_comment(t):
    r'\#([^\n])*'
    pass


def t_ANY_STRING(t):
    r'"'
    if t.lexer.current_state() == 'string':
        t.lexer.begin('INITIAL')
    else:
        t.lexer.begin('string')
    return t


t_string_STR = r'(\\.|[^"])+'
t_string_ignore = ''


def t_string_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_VAR(t):
    r'\$[A-Z]+\[\"[^\s]+\"\]'
    return t


def p_start(p):
    'start : statement_list'
    p[0] = p[1]


def p_statement_list(p):
    '''statement_list : statement_list statement
                      | empty'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = []


def p_statement(p):
    '''statement : assignment
                | statement_if
                | merge
                | include
                | include_shell'''
    p[0] = p[1]


def p_statement_if(p):
    '''statement_if : expr OPEN_BRACE statement_list CLOSE_BRACE
    '''
    p[0] = If(p[1], p[3], lineno=p.lineno(2))


def p_expr(p):
    '''expr : VAR op str
    '''
    p[0] = Op(p[1], p[3], p[2], lineno=p.lineno(1))


def p_merge(p):
    '''merge : option_name MERGE value
    '''
    p[0] = Concat(p[1], p[3], lvalue=True, lineno=p.lineno(2))


def p_op(p):
    '''op : EQUAL
          | NOT_EQUAL
          | RE_MATCH
          | RE_NOT_MATCH'''
    p[0] = p[1]


def p_assignment(p):
    '''assignment : option_name ASSIGN value
    '''
    p[0] = Assignment(p[1], p[3], lineno=p.lineno(2))


def p_include(p):
    '''include : INCLUDE value'''
    p[0] = Include(p[2], lineno=p.lineno(1))


def p_include_shell(p):
    '''include_shell : INCLUDE_SHELL str'''
    p[0] = Include(p[2], shell=True, lineno=p.lineno(1))


def p_value(p):
    '''value : str
             | INTEGER
             | BOOLEAN
             | array
             | option_name
             | value PLUS value'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Concat(p[1], p[3], lineno=p.lineno(1))


def p_array(p):
    '''array : OPEN_BRACKET array_item_list CLOSE_BRACKET
    '''
    p[0] = Array(p[2], lineno=p.lineno(1))


def p_array_item_list(p):
    '''
    array_item_list : array_item_list COMMA array_item
                    | array_item
                    | empty

    '''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [] if p[1] is None else [p[1]]


def p_array_item(p):
    '''array_item : str DOUBLE_ARROW value
                  | value'''
    if len(p) == 4:
        p[0] = ArrayItem(key=p[1], value=p[3], lineno=p.lineno(1))
    else:
        p[0] = ArrayItem(value=p[1], lineno=p.lineno(1))


def p_str(p):
    '''str : STRING STR STRING
            | STRING STRING'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = ""


def p_option_name(p):
    '''option_name : NAME'''
    p[0] = Option(p[1], lineno=p.lineno(1))


def p_empty(p):
    """empty : """
    pass


def p_error(p):
    print('Unexpected token:', p)


class Array:
    def __init__(self, items, lineno):
        self.items = items
        self.lineno = lineno

    def offset(self, key):
        for item in self.items:
            if item.key == key:
                return item.value
        return ''

    def __str__(self):
        return '(' + ','.join([str(item) for item in self.items]) + ')'


class ArrayItem:
    def __init__(self, value, lineno, key=None):
        self.value = value
        self.key = key
        self.lineno = lineno

    def __str__(self):
        if self.key is not None:
            return '"{}" => "{}"'.format(str(self.key), str(self.value))
        return self.value


class Concat:
    def __init__(self, left, right, lineno, lvalue=False):
        self.left = left,
        self.right = right,
        self.lvalue = lvalue
        self.lineno = lineno


class Assignment:
    def __init__(self, left, right, lineno):
        self.left = left
        self.right = right
        self.lineno = lineno


class Option:
    def __init__(self, name, lineno):
        self.name = name
        self.lineno = lineno


class Op:
    def __init__(self, left, right, op, lineno):
        self.left = left
        self.right = right
        self.op = op
        self.lineno = lineno


class If:
    def __init__(self, condition, statemets, lineno):
        self.condition = condition
        self.stmts = statemets
        self.lineno = lineno


class Include:
    def __init__(self, fname, lineno, shell=False):
        self.fname = fname
        self.shell = shell
        self.lineno = lineno


lexer = lex.lex()
parser = yacc.yacc(debug=False, write_tables=False)
