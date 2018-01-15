import json
import os
import sys


class Config:
    conftype = ''
    not_unique = []

    def __init__(self, fname, options):
        self.source = fname
        self.rules = []
        self._load_inner_rules()
        if options.user_rules:
            self.rules.extend(self._get_user_rules(self.load_rules(options.user_rules)))

    def getappdir(self):
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
            prod = os.path.join(application_path, '../config')
            dev = os.path.join(application_path, '../dist')
            return prod if os.path.exists(prod) else dev
        else:
            return os.path.join(os.path.dirname(__file__))

    def _load_inner_rules(self):
        self.rule_base = os.path.join(self.getappdir(), 'inner_rules/{}.js'.format(self.conftype))
        self.rules = self.load_rules(self.rule_base)

    def load_rules(self, fname):
        with open(os.path.realpath(fname), 'r') as f:
            ret = json.load(f)
        return ret

    def _get_user_rules(self, l):
        ret = []
        for rule in l:
            if rule['conftype'] == self.conftype:
                ret.append(rule)
        return ret

    def get_extended_context(self, context, extlist):
        pass

    def find_nodes(self, name, context=None):
        pass

    def is_unique_option(self, option):
        return False if option in self.not_unique else True


class MatchingNode:
    def __init__(self, name, value, lineno, node=None, attribute=False, source=None):
        self.name = name
        self.value = value
        self.lineno = lineno
        self.isattrib = attribute
        self.source = source
        self.node = node
