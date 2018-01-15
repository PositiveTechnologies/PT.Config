import os
from .run import run, vuln
import pytest

xfail = pytest.mark.xfail

b, m = os.path.realpath(os.path.join(os.path.dirname(__file__), 'input_bad/tomcat/server.xml')), os.path.realpath(
        os.path.join(os.path.dirname(__file__), 'input_missing/tomcat/server.xml'))
bad, missing = run(b), run(m)


def test_fp():
    assert len(bad) == 9
    assert len(missing) == 5


def test_xpoweredBy():
    expected = vuln('@xpoweredBy', 'true', 'false')
    assert expected in bad


def test_allowTrace():
    expected = vuln('@allowTrace', 'true', 'false')
    assert expected in bad


def test_shutdown():
    expected = vuln('@shutdown', 'SHUTDOWN', 'NONDETERMINISTICVALUE')
    assert expected in bad


def test_clientAuth():
    expected = vuln('@clientAuth', 'false', 'true')
    assert expected in bad


def test_secure():
    expected = vuln('@secure', 'false', 'true')
    assert expected in bad


def test_autoDeploy():
    expected = vuln('@autoDeploy', 'true', 'false')
    assert expected in bad


def test_deployOnStartup():
    expected = vuln('@deployOnStartup', 'true', 'false')
    assert expected in bad


def test_connectionTimeout():
    expected = vuln('@connectionTimeout', '-1', '60000')
    assert expected in bad


def test_maxHttpHeaderSize():
    expected = vuln('@maxHttpHeaderSize', '16384', '8192')
    assert expected in bad


def test_missing_shutdown():
    expected = vuln('@shutdown', 'not set', 'NONDETERMINISTICVALUE')
    assert expected in missing


def test_missing_clientAuth():
    expected = vuln('@clientAuth', 'not set', 'true')
    assert expected in missing


def test_missing_secure():
    expected = vuln('@secure', 'not set', 'true')
    assert expected in missing


def test_missing_autoDeploy():
    expected = vuln('@autoDeploy', 'not set', 'false')
    assert expected in missing


def test_missing_deployOnStartup():
    expected = vuln('@deployOnStartup', 'not set', 'false')
    assert expected in missing
