from lxml.etree import *
from baseconfig import Config, MatchingNode


class NotSuitable(Exception):
    pass


class XMLlikeConfig(Config):
    def __init__(self, path, options):
        Config.__init__(self, path, options)
        with open(path, 'rb') as f:
            data = f.read()
        self.config = fromstring(data.replace(b'\r', b''))
        self._strip_ns()
        if self.get_root_name() != self.root:
            raise NotSuitable("Unknown configuration type")

    def _strip_ns(self):
        for node in self.config.iter():
            try:
                has_namespace = node.tag.startswith('{')
            except AttributeError:
                continue
            if has_namespace:
                node.tag = node.tag.split('}', 1)[1]

    def get_root_name(self):
        return self.config.tag

    def get_extended_context(self, context, extlist):
        ret = []
        new_c = ''
        for option, value in extlist:
            new_c += '[{}="{}"]'.format(option, value)
        [ret.append(c + new_c) for c in context]
        return ret


    def find_nodes(self, name, context=None):
        ret = []
        isattr = name.startswith('@')
        realname = name if not isattr else name[1::]

        for c in context:
            path = c + ('[{}]'.format(name) if isattr else '/{}'.format(name))
            matching = self.config.findall(path)
            for node in matching:
                value = node.text if not isattr else node.attrib[realname]
                ret.append(MatchingNode(realname, value, node.sourceline, node=node, attribute=isattr))
        return ret

    def get_node_value(self, node):
        return node.value

    def get_lineno(self, node):
        return node.lineno

    def fill_missing_line(self, option, value, context=None):
        isattr = option.startswith('@')
        realname = option if not isattr else option[1::]

        directives = context[0].replace('./', self.get_root_name()).replace('[@', ' ').replace(']', '').split('/')

        if isattr:
            line = " " + realname + "=" + "\"%s\"" % value
            d = directives.pop()
            line = "<{}{}/>".format(d, line)
        else:
            line = "<{}>{}</{}>".format(realname, value, realname)
        directives.reverse()
        for d in directives:
            line = "<{}>{}</{}>".format(d, line, d)
        return line


class ApplicationHostConfig(XMLlikeConfig):
    conftype = 'applicationHost.config'

    def __init__(self, path, options):
        self.root = "configuration"
        XMLlikeConfig.__init__(self, path, options)


class DomainXml(XMLlikeConfig):
    conftype = 'domain.xml'
    not_unique = ['jvm-options']

    def __init__(self, path, options):
        self.root = "domain"
        XMLlikeConfig.__init__(self, path, options)


class MachineConfig(XMLlikeConfig):
    conftype = 'machine.config'

    def __init__(self, path, options):
        self.root = "configuration"
        XMLlikeConfig.__init__(self, path, options)


class ServerXml(XMLlikeConfig):
    def __init__(self, path, options):
        try:
            cls = Tomcat(path, options)
        except NotSuitable:
            try:
                cls = Websphere(path, options)
            except NotSuitable as e:
                raise e
        self.__class__ = cls.__class__
        self.__dict__ = cls.__dict__


class Tomcat(ServerXml):
    conftype = 'server.xml_tomcat'

    def __init__(self, path, options):
        self.root = "Server"
        XMLlikeConfig.__init__(self, path, options)


class Websphere(ServerXml):
    conftype = 'server.xml_websphere'

    def __init__(self, path, options):
        self.root = "server"
        XMLlikeConfig.__init__(self, path, options)


class StandaloneXml(XMLlikeConfig):
    conftype = 'standalone.xml'
    not_unique = ['module-option']

    def __init__(self, path, options):
        self.root = "server"
        XMLlikeConfig.__init__(self, path, options)


class WebConfig(XMLlikeConfig):
    conftype = 'web.config'
    not_unique = ['@statusCode', '@users']

    def __init__(self, path, options):
        self.root = "configuration"
        XMLlikeConfig.__init__(self, path, options)


class WebXml(XMLlikeConfig):
    conftype = 'web.xml'
    not_unique = ['error-code']

    def __init__(self, path, options):
        self.root = "web-app"
        XMLlikeConfig.__init__(self, path, options)
