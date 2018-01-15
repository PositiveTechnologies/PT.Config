import os
from .run import run, vuln
import pytest

xfail = pytest.mark.xfail

b, m, i = os.path.realpath(os.path.join(os.path.dirname(__file__), 'input_bad/lighttpd.conf')), os.path.realpath(
        os.path.join(os.path.dirname(__file__), 'input_missing/lighttpd.conf')), os.path.realpath(
        os.path.join(os.path.dirname(__file__), 'composite/include_lighttpd/lighttpd.conf'))
bad, missing, inc = run(b), run(m), run(i)


def test_fp():
    assert len(bad) == 6
    assert len(missing) == 3


def test_include():
    assert len(inc) == 1
    expected = vuln('status.config-url', '/server-config', '""')
    assert expected in inc


def test_server_dir_listing():
    expected = vuln('server.dir-listing', 'enable', 'disable')
    assert expected in bad


def test_status_status_url():
    expected = vuln('status.status-url', '/server-status', '""')
    assert expected in bad


def test_status_config_url():
    expected = vuln('status.config-url', '/server-config', '""')
    assert expected in bad


def test_setenv_add_response_header():
    expected = vuln('setenv.add-response-header',
                    '("X-Secret-Message" => "42")',
                    '(\"Strict-Transport-Security\" => \"max-age=%d; includeSubDomains\",\"X-XSS-Protection\" => \"1; mode=block\",\"X-Frame-Options\" => \"DENY\",\"Access-Control-Allow-Origin\" => \"http://%s\",\"X-Content-Type-Options\" => \"nosniff\",\"X-Download-Options\" => \"noopen\",\"Content-Security-Policy\" => \"default-src \'self\'\")',
                    )
    assert expected in bad


def test_cgi_assign():
    expected = vuln('cgi.assign', '(".pl" => "/usr/bin/perl",".cgi" => "/usr/bin/perl")',
                    '$HTTP["url"] =~ "^/cgi-bin/" {cgi.assign = (".pl"  => "/usr/bin/perl", ".py"  => "/usr/bin/python")}')
    assert expected in bad


def test_webdav_is_readonly():
    expected = vuln('webdav.is-readonly', 'disable', 'enable')
    assert expected in bad


def test_missing_server_dir_listing():
    expected = vuln('server.dir-listing', 'not set', 'disable')
    assert expected in missing


def test_missing_setenv_add_response_header():
    expected = vuln('setenv.add-response-header',
                    'not set',
                    '(\"Strict-Transport-Security\" => \"max-age=%d; includeSubDomains\",\"X-XSS-Protection\" => \"1; mode=block\",\"X-Frame-Options\" => \"DENY\",\"Access-Control-Allow-Origin\" => \"http://%s\",\"X-Content-Type-Options\" => \"nosniff\",\"X-Download-Options\" => \"noopen\",\"Content-Security-Policy\" => \"default-src \'self\'\")',
                    )
    assert expected in missing


def test_missing_webdav_is_readonly():
    expected = vuln('webdav.is-readonly', 'not set', 'enable')
    assert expected in missing
