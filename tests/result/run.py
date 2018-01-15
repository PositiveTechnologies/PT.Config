# !/usr/bin/env python

import os
import subprocess
from xml.dom.minidom import parseString
from collections import defaultdict, namedtuple

vuln = namedtuple('vuln', ['function', 'existing_value', 'recommended_value'])
os.chdir('../../src')


def run(src, **kwargs):
    repname = os.path.join(os.getenv('TEMP'), 'confresult.xml')
    runCore(src, repname, kwargs)
    ret = parseResult(repname)
    vulns = ret.getElementsByTagName("vuln")
    vulnList = getData(vulns, 'function', 'existing_value', 'recommended_value')
    return vulnList


def runCore(target, repname, kwargs):
    cmd = ['python', 'main.py', target, '-r', repname]
    if kwargs.get('user_rules'):
        cmd += ['--user-rules', kwargs['user_rules']]
    proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        outs, errs = proc.communicate(timeout=15)
    except subprocess.TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()
    return outs


def parseResult(rep):
    with open(rep, 'r+b') as report:
        ret = report.read()
    os.remove(rep)
    try:
        ret = parseString(ret)
    except:
        open('parseString.xml', 'wb').write(ret)
        raise
    return ret


def getData(items, *fields):
    rets = []
    for x in items:
        elem = {}
        for field in fields:
            elem[field] = getNodeValue(x, field)
        rets.append(vuln(**elem))
    return rets


def getNodeValue(node, value):
    ret = ''
    vals = node.getElementsByTagName(value)
    if not vals:
        return ''
    nodelist = vals[0].childNodes
    for node in nodelist:
        ret += node.data.strip()
    return ret
