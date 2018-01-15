import os
from .run import run, vuln
import pytest

xfail = pytest.mark.xfail

b, m = os.path.realpath(os.path.join(os.path.dirname(__file__), 'input_bad/web.xml')), os.path.realpath(
        os.path.join(os.path.dirname(__file__), 'input_missing/web.xml'))
bad, missing = run(b), run(m)


def test_fp():
    assert len(bad) == 8
    assert len(missing) == 15


def test_http_method():
    expected = vuln('http-method', 'GET', 'do not use')
    assert expected in bad


def test_transport_guarantee():
    expected = vuln('transport-guarantee', 'NONE', 'CONFIDENTIAL')
    assert expected in bad


def test_session_timeout():
    expected = vuln('session-timeout', '25', '15')
    assert expected in bad


def test_tracking_mode():
    expected = vuln('tracking-mode', 'URL', 'COOKIE')
    assert expected in bad


def test_http_only():
    expected = vuln('http-only', 'false', 'true')
    assert expected in bad


def test_secure():
    expected = vuln('secure', 'false', 'true')
    assert expected in bad


def test_param_value():
    expected = vuln('param-value', 'true', 'false')
    assert expected in bad


def test_disable_xsrf_protection():
    expected = vuln('param-value', 'true', 'false')
    assert expected in bad


def test_missing_session_timeout():
    expected = vuln('session-timeout', 'not set', '15')
    assert expected in missing


def test_missing_transport_guarantee():
    expected = vuln('transport-guarantee', 'not set', 'CONFIDENTIAL')
    assert expected in missing


def test_error_code_400():
    expected = vuln('error-code', 'not set', '400')
    assert expected in missing


def test_error_code_401():
    expected = vuln('error-code', 'not set', '401')
    assert expected in missing


def test_error_code_403():
    expected = vuln('error-code', 'not set', '403')
    assert expected in missing


def test_error_code_404():
    expected = vuln('error-code', 'not set', '404')
    assert expected in missing


def test_error_code_405():
    expected = vuln('error-code', 'not set', '405')
    assert expected in missing


def test_error_code_408():
    expected = vuln('error-code', 'not set', '408')
    assert expected in missing


def test_error_code_411():
    expected = vuln('error-code', 'not set', '411')
    assert expected in missing


def test_error_code_413():
    expected = vuln('error-code', 'not set', '413')
    assert expected in missing


def test_error_code_414():
    expected = vuln('error-code', 'not set', '414')
    assert expected in missing


def test_error_code_500():
    expected = vuln('error-code', 'not set', '500')
    assert expected in missing


def test_error_code_502():
    expected = vuln('error-code', 'not set', '502')
    assert expected in missing


def test_error_code_503():
    expected = vuln('error-code', 'not set', '503')
    assert expected in missing


def test_error_code_504():
    expected = vuln('error-code', 'not set', '504')
    assert expected in missing
