import hashlib
from xml.dom.minidom import Document, Attr

import log
from utils import *
import uitransport


class TransportManager:
    def __init__(self, options):
        self.options = options
        self.log = log.Log(options.logs_dir)
        try:
            self.pipe = uitransport.Bridge(_pipeName=self.options.pipe) if self.options.pipe else None
        except uitransport.BridgeException:
            self.log.write("Broken pipe {}".format(self.options.pipe))
            self.pipe = None
        if self.pipe:
            self.pipe.json_version = options.json_version
        self.reportMgr = ReportManager(self.options.report)
        self.nexploit = 0

    def stop(self):
        self.reportMgr.stop()

    def startFile(self):
        if self.pipe:
            self.pipe.OnStart()

    def stopFile(self):
        if self.pipe:
            self.pipe.OnStop()

    def sendPriorities(self):
        if self.pipe:
            self.pipe.PrepStart()
            self.pipe.SendPriorities(FileExtensions())
            self.pipe.PrepStop()

    def send(self, vuln):
        vuln.place = self._exploit_id(vuln)
        print(repr(vuln))
        self.reportMgr.add_vuln(vuln)
        self._send_vuln(vuln)

    def _send_vuln(self, vulner):
        if self.pipe:
            vuln = uitransport.Vulnerability()
            vuln.Exploit = vulner.exploit
            vuln.SourceFile = vulner.file
            vuln.Function = vulner.option
            vuln.ExistingValue = vulner.existing_value
            vuln.RecommendedValue = vulner.recommended_value
            vuln.NumberLine = vulner.lineno
            vuln.Place = vulner.place
            vuln.RawLine = vulner.line
            vuln.Type = vulner.type
            self.pipe.SendVulnerability(vuln)

    def _exploit_id(self, vuln):
        fid = hashlib.md5(vuln.file.encode('utf8')).hexdigest()[:8]
        eid = "%s-%d" % (fid, self.nexploit)
        self.nexploit += 1
        ret = "'%s'" % eid
        return ret


class ReportManager:
    def __init__(self, repname):
        self.report = repname
        if self.report:
            write_file(self.report, '')
            check_disk_free_space(os.path.realpath(self.report))

    def stop(self):
        if self.report:
            write_file(self.report, '<?xml version="1.1" encoding="UTF-8" ?>\n<report>\n%s\n</report>\n'
                       % open(self.report, 'r', encoding='utf-8').read())

    def add_vuln(self, vuln):
        if self.report:
            vulnstr = self.build_xml_str(vuln)
            append_file(self.report, vulnstr + '\n')

    def build_xml_str(self, vulner):
        doc = Document()
        vuln = doc.createElement('vuln')
        doc.appendChild(vuln)
        self._add_pair(doc, vuln, 'entry', vulner.entry)
        self._add_pair(doc, vuln, 'type', vulner.type)
        self._add_pair(doc, vuln, 'function', vulner.option)
        self._add_pair(doc, vuln, 'existing_value', vulner.existing_value)
        self._add_pair(doc, vuln, 'recommended_value', vulner.recommended_value)
        self._add_pair(doc, vuln, 'file', vulner.file)
        vulner.lineno = str(vulner.lineno)
        self._add_pair(doc, vuln, 'lineno', vulner.lineno)
        line = vulner.line if not isinstance(vulner.line, Attr) else vulner.line.value
        self._add_pair(doc, vuln, 'line', line, cdata=True)
        self._add_pair(doc, vuln, 'place', vulner.place)
        self._add_pair(doc, vuln, 'exploit', vulner.exploit)

        vulnstr = vuln.toprettyxml(indent='  ')
        return vulnstr

    def _add_pair(self, doc, parent, name, value, cdata=False):
        name = doc.createElement(name)
        parent.appendChild(name)
        if cdata:
            value = doc.createCDATASection(value)
        else:
            value = doc.createTextNode(value)
        name.appendChild(value)


class FileExtensions:
    def __init__(self):
        self.priority = 0
        self.extensions = ['conf', 'htaccess', 'config', 'xml', 'ini']


class Vuln:
    def __repr__(self):
        return """{}\nentry: {}\nfile: {}\noption: {}\ncurrent value: {}\nlineno: {}\nline: {}\nrecommended_value: {}\n{}""".format(
                "=" * 80, self.entry, self.file, self.option, self.existing_value, self.lineno, self.line,
                self.recommended_value, "=" * 80)


class MissingOption(Vuln):
    def __init__(self, entrypoint, exitpoint, type, option, rec, line):
        self.entry = entrypoint
        self.type = type
        self.option = option
        self.file = exitpoint
        self.lineno = -1
        self.line = line
        self.exploit = ''
        self.existing_value = "not set"
        self.recommended_value = rec if rec else "\"\""


class BadOption(Vuln):
    def __init__(self, entrypoint, exitpoint, type, option, existing, rec, lineno, line):
        self.entry = entrypoint
        self.type = type
        self.option = option
        self.file = exitpoint
        self.lineno = lineno
        self.line = line
        self.exploit = ''
        self.existing_value = str(existing)
        self.recommended_value = rec if rec else "\"\""
