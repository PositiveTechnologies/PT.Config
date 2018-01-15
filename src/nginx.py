import nginxparser
from baseconfig import Config, MatchingNode
import re


class Nginx(Config):
    conftype = 'nginx.conf'

    def __init__(self, path, options):
        Config.__init__(self, path, options)
        with open(path, 'r') as f:
            self.config = nginxparser.load(f)

    def _setlineno(self, l):
        i = 0
        name, value = l[i].name, l[i].value
        with open(self.source, "r") as searchfile:
            for number, line in enumerate(searchfile):
                if re.match(".*{}\s+{}.*".format(name, value), line):
                    l[i].lineno = number+1
                    i += 1
                    if i == len(l):
                        break
                    name, value = l[i].name, l[i].value
        return l

    def find_nodes(self, name, context=None):
        matched = []
        for c in context:
            ret = self._find(self.config, name, self._containers_by_context(c))
            if ret:
                ret = self._setlineno(ret)
            matched.extend(ret)
        return matched

    def _find(self, container, option, context=[]):
        if context:
            c = context.pop(0)
        else:
            c = ''
        ret = []
        for name, value in container:
            if isinstance(name, list) and name[0] == c:
                ret.extend(self._find(value, option, context))
            elif isinstance(name, str) and name == option and not c:
                ret.append(MatchingNode(name, value, 0))
        return ret

    def _containers_by_context(self, context):
        d = {
            'http': ['http'],
            'server': ['http', 'server'],
            'location': ['http', 'server', 'location']
        }
        try:
            return d[context]
        except KeyError:
            return []

    def fill_missing_line(self, option, value, context=None):
        line = '{} {};'.format(option, value)
        if isinstance(context, list):
            cl = self._containers_by_context(context[0])
            cl.reverse()
            for container in cl:
                line = container + '{ ' + line + ' }'
        return line
