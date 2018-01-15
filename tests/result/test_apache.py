import os
from .run import run, vuln
import pytest

xfail = pytest.mark.xfail

b, m, i = os.path.realpath(os.path.join(os.path.dirname(__file__), 'input_bad/apache.conf')), os.path.realpath(
        os.path.join(os.path.dirname(__file__), 'input_missing/apache.conf')), os.path.realpath(
        os.path.join(os.path.dirname(__file__), 'composite/include_apache/apache.conf'))
bad, missing, inc = run(b), run(m), run(i)


def test_fp():
    assert len(bad) == 14
    assert len(missing) == 3


def test_add_type_php():
    expected = vuln('AddType', 'application/x-httpd-php .htaccess', 'SetHandler application/x-httpd-php')
    assert expected in bad


def test_add_type_suphp():
    expected = vuln('AddType', 'application/x-httpd-suphp .htaccess', 'do not use')
    assert expected in bad


def test_add_handler():
    expected = vuln('AddHandler', 'application/x-httpd-php .htaccess', 'SetHandler application/x-httpd-php')
    assert expected in bad


def test_server_tokens():
    expected = vuln('ServerTokens', 'Full', 'Prod')
    assert expected in bad


def test_trace_enable():
    expected = vuln('TraceEnable', 'On', 'off')
    assert expected in bad


def test_server_signature():
    expected = vuln('ServerSignature', 'On', 'off')
    assert expected in bad


def test_autoindex_module():
    expected = vuln('LoadModule', 'autoindex_module   libexec/apache/mod_autoindex.so', 'do not use')
    assert expected in bad


def test_negotiation_module():
    expected = vuln('LoadModule', 'negotiation_module libexec/apache/mod_negotiation.so', 'do not use')
    assert expected in bad


def test_info_module():
    expected = vuln('LoadModule', 'info_module        libexec/apache/mod_info.so', 'do not use')
    assert expected in bad


def test_cgi_module():
    expected = vuln('LoadModule', 'cgi_module         libexec/apache/mod_cgi.so', 'do not use')
    assert expected in bad


def test_include_module():
    expected = vuln('LoadModule', 'include_module	  modules/mod_include.so', 'do not use')
    assert expected in bad


def test_options():
    expected = vuln('Options', '+Indexes +ExecCGI +Includes', '-Indexes -ExecCGI -Includes -Multiviews')
    assert expected in bad


def test_php_value_auto_prepend_file():
    expected = vuln('php_value', 'auto_prepend_file /tmp/backdoor.php', 'do not use')
    assert expected in bad


def test_php_value_auto_append_file():
    expected = vuln('php_value', 'auto_append_file /tmp/backdoor.php', 'do not use')
    assert expected in bad


def test_missing_server_tokens():
    expected = vuln('ServerTokens', 'not set', 'Prod')
    assert expected in missing


def test_missing_trace_enable():
    expected = vuln('TraceEnable', 'not set', 'off')
    assert expected in missing


def test_missing_security2_module():
    expected = vuln('LoadModule', 'not set', 'security2_module')
    assert expected in missing


def test_include():
    assert len(inc) == 1
    expected = vuln('Options', '+Indexes +ExecCGI +Includes', '-Indexes -ExecCGI -Includes -Multiviews')
    assert expected in inc
