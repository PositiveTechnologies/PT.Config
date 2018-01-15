import re
import sys
import os
from json import JSONDecodeError
from log import Log
from options import options, args
from utils import *
from configs import *
from httpgen import TransportManager, MissingOption, BadOption


class ConfigAnalyzer:
    def __init__(self, options):
        self.fmapping = {
            'apache.conf': Apache,
            'apache2.conf': Apache,
            'httpd.conf': Apache,
            '.htaccess': Htaccess,
            'applicationhost.config': ApplicationHostConfig,
            'domain.xml': DomainXml,
            'lighttpd.conf': Lighttpd,
            'machine.config': MachineConfig,
            'nginx.conf': Nginx,
            'php.ini': Php,
            'server.xml': ServerXml,
            'standalone.xml': StandaloneXml,
            'web.config': WebConfig,
            'web.xml': WebXml
        }
        self.log = Log(options.logs_dir)
        self.matcher = Matcher(self.log)
        check_disk_free_space(self.log.HOMEDIR)
        self.options = options
        self.transporter = TransportManager(self.options)

    def preprocessing(self):
        self.transporter.sendPriorities()

    def scandir(self, path):
        self.log.write('sys.argv=%s' % repr(sys.argv))
        if os.path.isdir(path):
            for top, dirs, files in os.walk(path):
                for nm in files:
                    self._scanfile(os.path.join(top, nm))
        elif os.path.isfile(path):
            self._scanfile(path)
        else:
            self.log.write("Scan target {} does not exist".format(path))
        self.transporter.stop()

    def _scanfile(self, fname):
        try:
            self.transporter.startFile()
            basename = os.path.basename(fname)
            config = self.fmapping[basename.lower()](fname, self.options)
            self.log.write("Processing: %s" % config.source)
            self._scan(config)
        except KeyError:
            pass
        except OSError as e:
            self.log.write(e)
        except JSONDecodeError as e:
            self.log.write('Invalid user rules formatting: {}'.format(e))
        except Exception as e:
            self.log.write("%s" % e)
            self.log.exc()
        finally:
            self.transporter.stopFile()

    def _scan(self, config):
        for rule in config.rules:
            if isinstance(rule, list):
                self._apply_composite_rule(config, rule)
            else:
                ret = self.matcher.match(config, Rule(rule))
                if ret:
                    self.alert(ret)

    def _apply_composite_rule(self, config, rules):
        rules = [Rule(r) for r in rules]
        xpaths = []
        [xpaths.extend(r.xpath()) for r in rules]
        names = [r.name() for r in rules]
        unique_xpaths, unique_names = set(xpaths), set(names)
        if len(unique_xpaths) == 1 and len(unique_names) > 1:
            suspects = self.matcher.match(config, rules.pop(0))
            for suspect in suspects:
                ret = [self.matcher.match(config, r, extended_context=config.get_extended_context(r.xpath(),
                                                        [(suspect.option, suspect.existing_value)])) for r in rules]
                if all(ret):
                    self.alert(ret[-1])
        else:
            ret = [self.matcher.match(config, r) for r in rules]
            if all(ret):
                self.alert(ret[-1])

    def alert(self, vulnlist):
        [self.transporter.send(vuln) for vuln in vulnlist]


class Matcher:
    OK = 0
    SKIP = 1
    ALERT = 2

    def __init__(self, log):
        self.log = log

    def match(self, config, rule, extended_context=''):
        suspects = config.find_nodes(rule.name(), context=extended_context if extended_context else rule.xpath())
        unique_option = config.is_unique_option(rule.name())
        found = True if unique_option else False

        vl = []
        for suspect in suspects:
            ret = self.compare(suspect.value, rule, is_unique=unique_option)
            if ret == self.ALERT:
                exitpoint = config.source if not suspect.source else suspect.source
                vuln = BadOption(entrypoint=config.source,
                                 exitpoint=exitpoint,
                                 type=rule.id(), option=rule.name(), existing=suspect.value,
                                 rec=rule.recommended_value(), lineno=suspect.lineno,
                                 line=file_line(exitpoint, suspect.lineno))
                vl.append(vuln)
            elif ret == self.SKIP:
                continue
            elif ret == self.OK:
                found = True

        if not suspects or not found:
            ret = self.compare(rule.default_value(), rule, is_unique=unique_option)
            if ret != self.OK:
                return [MissingOption(entrypoint=config.source, exitpoint=config.source,
                                      type=rule.id(), option=rule.name(), rec=rule.recommended_value(),
                                      line=config.fill_missing_line(rule.name(), rule.recommended_value(),
                                                                    extended_context if extended_context else rule.xpath()))]

        return vl

    def compare(self, existing, rule, is_unique=True):
        nr = rule.not_recommended_values()
        op = rule.comparison_type()
        cm = rule.comparison_method()
        regexp = rule.regexp()

        if nr:
            rets = [self.do_op(v, existing, op) for v in nr]
            if eval("{}({})".format(cm, rets)):
                return self.ALERT
            return self.OK
        r = rule.recommended_values()
        values = regexp if regexp else r
        rets = [self.do_op(v, existing, op) for v in values]
        if eval("{}({})".format(cm, rets)):
            return self.OK
        return self.ALERT if is_unique else self.SKIP

    def do_op(self, left, right, op):
        if isinstance(left, dict):
            return self.do_op_array(left, right, op)
        return self.do_op_simple(left, right, op)

    def do_op_array(self, left, right, op):
        if not hasattr(right, 'offset'):
            return False
        if op == 'equal':
            if len(right.items) != len(left):
                return False
            for key, value in left.items():
                if right.offset(key) == value:
                    continue
                return False
            return True
        elif op == 'in':
            for key, value in left.items():
                if right.offset(key) == value:
                    continue
                return False
            return True
        elif op in ['<=', '>=', 'regexp']:
            for key, value in left.items():
                if self.do_op_simple(value, right.offset(key), op):
                    continue
                return False
            return True
        else:
            self.log.write("Unsupported comparison type {}".format(op))

    def do_op_simple(self, left, right, op):
        if op == 'equal':
            return True if str(left).lower() == str(right).lower() else False
        elif op == 'in':
            return True if str(left) in str(right) else False
        elif op in ['<=', '>=', '>', '<']:
            factor = {'k': 1024, 'm': 1024 ** 2, 'g': 1024 ** 3}
            l = re.match("-?(\d+)(.*)", left)
            r = re.match("-?(\d+)(.*)", right)
            fl = l.group(2).lower()
            fr = r.group(2).lower()
            r = int(r.group(1))
            l = int(l.group(1))
            if fr:
                try:
                    r *= int(factor[fr])
                except KeyError:
                    pass
            if fl:
                try:
                    l *= int(factor[fl])
                except KeyError:
                    pass

            return eval("{}{}{}".format(r, op, l))
        elif op == 'regexp':
            pattern = re.compile(left)
            return True if pattern.match(str(right)) else False
        else:
            self.log.write("Unsupported comparison type {}".format(op))


class Rule:
    def __init__(self, rule):
        self.rule = rule
        self.log = Log(options.logs_dir)

    def name(self):
        try:
            ret = self.rule['name'].split('[')[0]
            return ret
        except KeyError:
            self.log.write("Option name is missing in rule {}".format(self.rule))

    def id(self):
        try:
            ret = self.type() + ' ' + self.rule['name']
            return ret
        except KeyError:
            self.log.write("Option name is missing in rule {}".format(self.rule))

    def xpath(self):
        try:
            ret = self.rule['xpath']
            return [ret] if not isinstance(ret, list) else ret
        except KeyError:
            return ''

    def comparison_type(self):
        try:
            return self.rule['comparison_type']
        except KeyError:
            return 'equal'

    def comparison_method(self):
        try:
            return self.rule['comparison_method']
        except KeyError:
            return 'any'

    def default_value(self):
        try:
            ret = self.rule['default']
            return ret
        except KeyError:
            self.log.write("Default value is missing in rule {}".format(self.rule))

    def recommended_values(self):
        try:
            ret = self.rule['recommended']
            return [ret] if not isinstance(ret, list) else ret
        except KeyError:
            self.log.write("Recommended value is missing in rule {}".format(self.rule))

    def recommended_value(self):
        if self.comparison_method() == 'all':
            return ', '.join(self.recommended_values())
        return self.recommended_values()[0]

    def not_recommended_values(self):
        try:
            ret = self.rule['not_recommended']
            return [ret] if not isinstance(ret, list) else ret
        except KeyError:
            return []

    def regexp(self):
        try:
            ret = self.rule['regexp']
            return [ret] if not isinstance(ret, list) else ret
        except KeyError:
            if self.comparison_type() == 'regexp':
                self.log.write("Regular expression is missing in rule {}".format(self.rule))

    def type(self):
        try:
            return self.rule['conftype']
        except KeyError:
            self.log.write("Config type is missing in rule {}".format(self.rule))
            return ''


if __name__ == '__main__':
    c = ConfigAnalyzer(options)
    if options.preprocessing:
        c.preprocessing()
    else:
        c.scandir(args[0])
