import os
from .run import run, vuln
import pytest

xfail = pytest.mark.xfail

b, m = os.path.realpath(os.path.join(os.path.dirname(__file__), 'input_bad/applicationHost.config')), os.path.realpath(
        os.path.join(os.path.dirname(__file__), 'input_missing/applicationHost.config'))
bad, missing = run(b), run(m)


def test_fp():
    assert len(bad) == 3
    assert len(missing) == 1


def test_userName():
    expected = vuln('@userName', 'IUSR', '""')
    assert expected in bad


def test_accessPolicy():
    expected = vuln('@accessPolicy', 'Read, Script, Execute, Write', 'Read')
    assert expected in bad


def test_notListedIsapisAllowed():
    expected = vuln('@notListedIsapisAllowed', 'true', 'false')
    assert expected in bad


def test_missing_userName():
    expected = vuln('@userName', 'not set', '""')
    assert expected in missing
