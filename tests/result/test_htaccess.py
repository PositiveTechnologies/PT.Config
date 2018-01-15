import os
from .run import run, vuln
import pytest

xfail = pytest.mark.xfail

b, m = os.path.realpath(os.path.join(os.path.dirname(__file__), 'input_bad/.htaccess')), os.path.realpath(
    os.path.join(os.path.dirname(__file__), 'input_missing/.htaccess'))
bad, missing = run(b), run(m)

def test_fp():
    assert len(bad) == 7
    assert len(missing) == 0


def test_add_type_php():
    expected = vuln('AddType', 'application/x-httpd-php .htaccess', 'SetHandler application/x-httpd-php')
    assert expected in bad


def test_add_type_suphp():
    expected = vuln('AddType', 'application/x-httpd-suphp .htaccess', 'do not use')
    assert expected in bad


def test_add_handler():
    b = bad
    expected = vuln('AddHandler', 'application/x-httpd-php .htaccess', 'SetHandler application/x-httpd-php')
    assert expected in bad


def test_options_indexes():
    expected = vuln('Options', 'Indexes ExecCGI Includes', '-Indexes -ExecCGI -Includes -Multiviews')
    assert expected in bad


def test_php_value_auto_prepend_file():
    expected = vuln('php_value', 'auto_prepend_file /tmp/backdoor.php', 'do not use')
    assert expected in bad


def test_php_value_auto_append_file():
    expected = vuln('php_value', 'auto_append_file /tmp/backdoor.php', 'do not use')
    assert expected in bad


def test_server_signature():
    expected = vuln('ServerSignature', 'On', 'off')
    assert expected in bad
