import os
from .run import run, vuln
import pytest

xfail = pytest.mark.xfail

b, m = os.path.realpath(os.path.join(os.path.dirname(__file__), 'input_bad/domain.xml')), os.path.realpath(
        os.path.join(os.path.dirname(__file__), 'input_missing/domain.xml'))
bad, missing = run(b), run(m)


def test_fp():
    assert len(bad) == 4
    assert len(missing) == 4


def test_audit_enabled():
    expected = vuln('@audit-enabled', 'false', 'true')
    assert expected in bad


def test_value():
    expected = vuln('@value', 'false', 'true')
    assert expected in bad


def test_port():
    expected = vuln('@port', '4848', '4847')
    assert expected in bad


def test_xpowered_by():
    expected = vuln('@xpowered-by', 'true', 'false')
    assert expected in bad


def test_missing_jvm_options():
    expected = vuln('jvm-options', 'not set', '-Djava.security.manager')
    assert expected in missing


def test_missing_audit_enabled():
    expected = vuln('@audit-enabled', 'not set', 'true')
    assert expected in missing


def test_missing_value():
    expected = vuln('@value', 'not set', 'true')
    assert expected in missing


def test_missing_port():
    expected = vuln('@port', 'not set', '4847')
    assert expected in missing
