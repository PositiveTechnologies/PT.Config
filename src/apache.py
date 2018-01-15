import os
import re
import glob
from baseconfig import Config


class Apache(Config):
    conftype = "apache.conf"
    not_unique = ['LoadModule']

    def __init__(self, fname, options):
        Config.__init__(self, fname, options)
        self.config = ApacheParser().parse(fname)

    def find_nodes(self, name, context=None):
        """
        Find nodes with the specified name

        @type  name: string
        @param name: Node name (can be written as path)

        @rtype: list
        @return: list of matched nodes
        """
        if self is None:
            return

        if not context:
            return self.config.container.find_nodes(name)
        found = []
        [found.extend(self.config.container.find_nodes(name, c)) for c in context]
        return found

    def fill_missing_line(self, option, value, context=None):
        return option + " " + value


class Htaccess(Apache):
    conftype = ".htaccess"


class ApacheParser:
    def __init__(self):
        self.container = Container()
        self.container.complete = True
        self.stack = [self.container]

    def parse(self, path, this_fname=None):
        """
        Load & parse configuration file

        @type  path: string
        @param path: configuration file path

        @rtype: self

        @raise: Exception
        """
        fp = open(path)
        global flist
        flist = []
        container = self.stack.pop()

        lineno = 0
        for line in fp:
            lineno = lineno + 1
            line = line.strip()
            if not line:
                continue

            node = self._get_node_instance(line)
            className = node.__class__.__name__

            if className == 'Container':
                self.stack.append(container)
                container = node
                continue

            elif className == 'ContainerEnd':
                if node.name.lower() != container.name.lower():
                    raise Exception('Unexpected directive name "%s"' % node.name)

                container.complete = True
                node = container
                container = self.stack.pop()

            elif className == 'Directive':
                name = node.name.lower()
                node.lineno = lineno
                node.line = line
                if name == "include" or name == "includepptional":
                    pattern = os.path.dirname(path) + '/' + node.value
                    if pattern[-1:] == '/':
                        pattern += '*'

                    for p in glob.glob(pattern):
                        self.stack.append(container)
                        if p.replace('/', '\\') in flist:
                            flist.remove(p.replace('/', '\\'))
                        self.parse(p, p)

                    continue

            elif className == 'Comment':
                continue

            if this_fname:
                node.source = os.path.normpath(this_fname)
            container.addNode(node)

        if not self.container.nodes:
            return None

        return self

    def _get_node_instance(self, line):
        """
        Search class for directive and return his instance

        @type  line: string
        @param line: directive

        @rtype:  Node
        @return: matched instance
        """
        node_classes = [Comment, Directive, Container, ContainerEnd, Node]
        for cls in node_classes:
            result = cls.match(line)
            if result:
                return result


class Node:
    # matchRe = re.compile(r'(.*)')

    def __init__(self):
        self.name = ''
        self.value = ''
        self.source = None

    @classmethod
    def match(self, line):
        """
        Find class for directive

        @type   line: string
        @param  line: configuration line

        @rtype  : Node or False
        @return : return object of matched class
        """
        match = self.matchRe.match(line)
        if not match:
            return False
        # nm = match.groupdict().get('name')
        # if nm not in allowedDirectives:
        #     raise Exception("Unknown directive name")

        obj = self()
        obj.populateFromMatch(match)
        return obj

    def populateFromMatch(self, match):
        """
        Fill object properties
        
        @type  match: MatchObject
        """
        self.value = match.group(1)

    def find_nodes(self, name, context=None):
        return []

    def __str__(self):
        """
        Return string representation of node

        @rtype: string
        """
        return self.value


class Comment(Node):
    matchRe = re.compile(r'^#(.*)$')

    def __init__(self):
        self.name = ''

    def populateFromMatch(self, match):
        """
        Fill object properties
        
        @type  match: MatchObject
        """
        self.value = match.group(1)

    def find_nodes(self, name, context=None):
        return []

    def __str__(self):
        """
        Return string representation of node

        @rtype: string
        """
        return '#' + self.value


class Directive(Node):
    matchRe = re.compile(r'^(?P<name>[A-Za-z_0-9]+)\s+(?P<value>.*)$')
    lineno = -1
    line = ''
    fname = None

    def populateFromMatch(self, match):
        """
        Fill object properties
        
        @type  match: MatchObject
        """
        self.name = match.group("name")
        self.value = match.group("value")

    def find_nodes(self, name, context=None):
        if self is None:
            return
        return [self] if self.name == name else []

    def __str__(self):
        """
        Return string representation of node

        @rtype: string
        """
        return self.name + ' ' + self.value


class Container(Node):
    matchRe = re.compile(r'^<(?P<name>[A-Za-z_0-9]+)\s*(?P<value>.*)>$')
    fname = None

    def __init__(self):
        self.complete = False
        self.nodes = []
        self.name = ''
        self.value = ''

    def populateFromMatch(self, match):
        """
        Fill object properties
        
        @type  match: MatchObject
        """
        self.name = match.group("name")
        self.value = match.group("value")

    def addNode(self, node):
        """
        Append node to container
        
        @type node: Node
        """
        self.nodes.append(node)

    def find_nodes(self, name, context=None):
        """
        Find nodes with the specified name

        @type  parts: list
        @param parts: list of node names

        @rtype: list
        @return: list of matched nodes
        """
        if self is None:
            return

        if self.name == context:
            return [self]

        results = []
        for node in self.nodes:
            res = None
            if context == 'ServerConfig':
                if isinstance(node, Directive):
                    res = node.find_nodes(name)
            elif context:
                filtered = node.find_nodes(context, context)
                for dir in filtered:
                    res = dir.find_nodes(name)
            else:
                res = node.find_nodes(name)
            if res is not None:
                results.extend(res)

        return results

    def __str__(self):
        """
        Return string representation of container

        @rtype: string
        """
        string = ""

        if self.name:
            string = "<%s%s>\n" % (self.name, ' ' + self.value)

        for node in self.nodes:
            string += node.__str__() + "\n"

        if self.name:
            string += "</%s>" % self.name

        return string


class ContainerEnd(Node):
    matchRe = re.compile(r'^</([A-Za-z_0-9]+)>$')

    def populateFromMatch(self, match):
        """
        Fill object properties
        
        @type  match: MatchObject
        """
        self.name = match.group(1)


allowedDirectives = [
    None, "AcceptMutex", "AcceptPathInfo", "AccessFileName", "Action", "AddAlt", "AddAltByEncoding", "AddAltByType",
    "AddCharset", "AddDefaultCharset", "AddDescription", "AddEncoding", "AddHandler", "AddIcon", "AddIconByEncoding",
    "AddIconByType", "AddInputFilter", "AddLanguage", "AddModuleInfo", "AddOutputFilter", "AddOutputFilterByType",
    "AddType", "Alias", "AliasMatch", "Allow", "allow", "AllowCONNECT", "AllowEncodedSlashes",
    "AllowOverride", "Anonymous", "Anonymous_Authoritative", "Anonymous_LogEmail", "Anonymous_MustGiveEmail",
    "Anonymous_NoUserID", "Anonymous_VerifyEmail", "AssignUserID", "AuthAuthoritative", "AuthDBMAuthoritative",
    "AuthDBMGroupFile", "AuthDBMType", "AuthDBMUserFile", "AuthDigestAlgorithm", "AuthDigestDomain", "AuthDigestFile",
    "AuthDigestGroupFile", "AuthDigestNcCheck", "AuthDigestNonceFormat", "AuthDigestNonceLifetime", "AuthDigestQop",
    "AuthDigestShmemSize", "AuthGroupFile", "AuthLDAPAuthoritative", "AuthLDAPBindDN", "AuthLDAPBindPassword",
    "AuthLDAPCharsetConfig", "AuthLDAPCompareDNOnServer", "AuthLDAPDereferenceAliases", "AuthLDAPEnabled",
    "AuthLDAPFrontPageHack", "AuthLDAPGroupAttribute", "AuthLDAPGroupAttributeIsDN", "AuthLDAPRemoteUserIsDN",
    "AuthLDAPUrl", "AuthName", "AuthType", "AuthUserFile", "BrowserMatch", "BrowserMatchNoCase", "BS2000Account",
    "BufferedLogs", "CacheDefaultExpire", "CacheDirLength", "CacheDirLevels", "CacheDisable", "CacheEnable",
    "CacheExpiryCheck", "CacheFile", "CacheForceCompletion", "CacheGcClean", "CacheGcDaily", "CacheGcInterval",
    "CacheGcMemUsage", "CacheGcUnused", "CacheIgnoreCacheControl", "CacheIgnoreHeaders", "CacheIgnoreNoLastMod",
    "CacheLastModifiedFactor", "CacheMaxExpire", "CacheMaxFileSize", "CacheMinFileSize", "CacheNegotiatedDocs",
    "CacheRoot", "CacheSize", "CacheTimeMargin", "CGIMapExtension", "CharsetDefault", "CharsetDisable" "CharsetOptions",
    "CharsetSourceEnc", "CheckSpelling", "ChildPerUserID", "ContentDigest", "CookieDomain", "CookieExpires",
    "CookieLog", "CookieName", "CookieStyle", "CookieTracking", "CoreDumpDirectory", "CustomLog", "Dav",
    "DavDepthInfinity", "DavLockDB", "DavMinTimeout", "DefaultIcon", "DefaultLanguage", "DefaultType",
    "DeflateBufferSize", "DeflateCompressionLevel", "DeflateFilterNote", "DeflateMemLevel", "DeflateWindowSize", "Deny",
    "deny",
    "Directory", "DirectoryIndex", "DirectoryMatch", "DirectorySlash", "DocumentRoot", "DumpIOInput", "DumpIOOutput",
    "EnableExceptionHook", "EnableMMAP", "EnableSendfile", "ErrorDocument", "ErrorLog", "Example", "ExpiresActive",
    "ExpiresByType", "ExpiresDefault", "ExtendedStatus", "ExtFilterDefine", "ExtFilterOptions", "FileETag", "Files",
    "FilesMatch", "ForceLanguagePriority", "ForceType", "ForensicLog", "Group", "Header", "HeaderName",
    "HostnameLookups", "IdentityCheck", "IfDefine", "IfModule", "IfVersion", "ImapBase", "ImapDefault", "ImapMenu",
    "Include", "IndexIgnore", "IndexOptions", "IndexOrderDefault", "ISAPIAppendLogToErrors", "ISAPIAppendLogToQuery",
    "ISAPICacheFile", "ISAPIFakeAsync", "ISAPILogNotSupported", "ISAPIReadAheadBuffer", "KeepAlive", "KeepAliveTimeout",
    "LanguagePriority", "LDAPCacheEntries", "LDAPCacheTTL", "LDAPConnectionTimeout", "LDAPOpCacheEntries",
    "LDAPOpCacheTTL", "LDAPSharedCacheFile", "LDAPSharedCacheSize", "LDAPTrustedCA", "LDAPTrustedCAType",
    "Limit", "LimitExcept", "LimitInternalRecursion", "LimitRequestBody", "LimitRequestFields", "LimitRequestFieldSize",
    "LimitRequestLine", "LimitXMLRequestBody", "Listen", "ListenBackLog", "LoadFile", "LoadModule", "Location",
    "LocationMatch", "LockFile", "LogFormat", "LogLevel", "MaxClients", "MaxKeepAliveRequests", "MaxMemFree",
    "MaxRequestsPerChild", "MaxRequestsPerThread", "MaxSpareServers", "MaxSpareThreads", "MaxThreads",
    "MaxThreadsPerChild", "MCacheMaxObjectCount", "MCacheMaxObjectSize", "MCacheMaxStreamingBuffer",
    "MCacheMinObjectSize", "MCacheRemovalAlgorithm", "MCacheSize", "MetaDir", "MetaFiles", "MetaSuffix",
    "MimeMagicFile", "MinSpareServers", "MinSpareThreads", "MMapFile", "ModMimeUsePathInfo", "MultiviewsMatch",
    "NameVirtualHost", "NoProxy", "NumServers", "NWSSLTrustedCerts", "NWSSLUpgradeable", "Options", "Order", "PassEnv",
    "php_value", "php_flag", "php_admin_value", "php_admin_flag",
    "PidFile", "ProtocolEcho", "Proxy", "ProxyBadHeader", "ProxyBlock", "ProxyDomain", "ProxyErrorOverride",
    "ProxyFtpDirCharset", "ProxyIOBufferSize", "ProxyMatch", "ProxyMaxForwards", "ProxyPass", "ProxyPassReverse",
    "ProxyPreserveHost", "ProxyReceiveBufferSize", "ProxyRemote", "ProxyRemoteMatch", "ProxyRequests", "ProxyTimeout",
    "ProxyVia", "ReadmeName", "ReceiveBufferSize", "Redirect", "RedirectMatch", "RedirectPermanent", "RedirectTemp",
    "RemoveCharset", "RemoveEncoding", "RemoveHandler", "RemoveInputFilter", "RemoveLanguage", "RemoveOutputFilter",
    "RemoveType", "RequestHeader", "Require", "RewriteBase", "RewriteCond", "RewriteEngine", "RewriteLock",
    "RewriteLog", "RewriteLogLevel", "RewriteMap", "RewriteOptions", "RewriteRule", "RLimitCPU", "RLimitMEM",
    "RLimitNPROC", "Satisfy", "ScoreBoardFile", "Script", "ScriptAlias", "ScriptAliasMatch", "ScriptInterpreterSource",
    "ScriptLog", "ScriptLogBuffer", "ScriptLogLength", "ScriptSock", "SecureListen", "SendBufferSize", "ServerAdmin",
    "ServerAlias", "ServerLimit", "ServerName", "ServerPath", "ServerRoot", "ServerSignature", "ServerTokens", "SetEnv",
    "SetEnvIf", "SetEnvIfNoCase", "SetHandler", "SetInputFilter", "SetOutputFilter", "SSIEndTag", "SSIErrorMsg",
    "SSIStartTag", "SSITimeFormat", "SSIUndefinedEcho", "SSLCACertificateFile", "SSLCACertificatePath",
    "SSLCARevocationFile", "SSLCARevocationPath", "SSLCertificateChainFile", "SSLCertificateFile",
    "SSLCertificateKeyFile", "SSLCipherSuite", "SSLEngine", "SSLMutex", "SSLOptions", "SSLPassPhraseDialog",
    "SSLProtocol", "SSLProxyCACertificateFile", "SSLProxyCACertificatePath", "SSLProxyCARevocationFile",
    "SSLProxyCARevocationPath", "SSLProxyCipherSuite", "SSLProxyEngine", "SSLProxyMachineCertificateFile",
    "SSLProxyMachineCertificatePath", "SSLProxyProtocol", "SSLProxyVerify", "SSLProxyVerifyDepth", "SSLRandomSeed",
    "SSLRequire", "SSLRequireSSL", "SSLSessionCache", "SSLSessionCacheTimeout", "SSLUserName", "SSLVerifyClient",
    "SSLVerifyDepth", "StartServers", "StartThreads", "SuexecUserGroup", "ThreadLimit", "ThreadsPerChild",
    "ThreadStackSize", "Timeout", "TraceEnable", "TransferLog", "TypesConfig", "UnsetEnv", "UseCanonicalName",
    "User", "UserDir", "VirtualDocumentRoot", "VirtualDocumentRootIP", "VirtualHost", "VirtualScriptAlias",
    "VirtualScriptAliasIP", "Win32DisableAcceptEx", "XBitHack"
]
