import os
from .run import run, vuln
import pytest

xfail = pytest.mark.xfail

b, m = os.path.realpath(os.path.join(os.path.dirname(__file__), 'input_bad/websphere/server.xml')), os.path.realpath(
        os.path.join(os.path.dirname(__file__), 'input_missing/websphere/server.xml'))
bad, missing = run(b), run(m)


def test_fp():
    assert len(bad) == 3
    assert len(missing) == 0


def test_allowLogoutPageRedirectToAnyHost():
    expected = vuln('@allowLogoutPageRedirectToAnyHost', 'true', 'false')
    assert expected in bad


def test_displayAuthenticationRealm():
    expected = vuln('@displayAuthenticationRealm', 'true', 'false')
    assert expected in bad


def test_add_type_suphp():
    expected = vuln('@preserveFullyQualifiedReferrerUrl', 'true', 'false')
    assert expected in bad
