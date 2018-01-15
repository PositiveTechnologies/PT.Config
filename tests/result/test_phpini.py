import os
from .run import run, vuln
import pytest

xfail = pytest.mark.xfail

b, m = os.path.realpath(os.path.join(os.path.dirname(__file__), 'input_bad/php.ini')), os.path.realpath(
    os.path.join(os.path.dirname(__file__), 'input_missing/php.ini'))
bad, missing = run(b), run(m)


def test_fp():
    assert len(bad) == 32
    assert len(missing) == 16


def test_allow_url_fopen():
    expected = vuln('allow_url_fopen', '1', '0')
    assert expected in bad


def test_allow_url_include():
    expected = vuln('allow_url_include', '1', '0')
    assert expected in bad


def test_assert_active():
    expected = vuln('assert.active', '1', '0')
    assert expected in bad


def test_auto_append_file():
    expected = vuln('auto_append_file', 'some_file', '""')
    assert expected in bad


def test_auto_prepend_file():
    expected = vuln('auto_prepend_file', 'some_file', '""')
    assert expected in bad


def test_cgi_fix_pathinfo():
    expected = vuln('cgi.fix_pathinfo', '1', '0')
    assert expected in bad


def test_disable_functions():
    expected = vuln('disable_functions', '',
                    'popen, exec, system, passthru, proc_open, shell_exec, apache_setenv, putenv, dl, expect_popen, pcntl_exec')
    assert expected in bad


def test_display_errors():
    expected = vuln('display_errors', '1', '0')
    assert expected in bad


def test_display_startup_errors():
    expected = vuln('display_startup_errors', '1', '0')
    assert expected in bad


def test_enable_dl():
    expected = vuln('enable_dl', '1', '0')
    assert expected in bad


def test_expose_php():
    expected = vuln('expose_php', '1', '0')
    assert expected in bad


def test_log_errors():
    expected = vuln('log_errors', '0', '1')
    assert expected in bad



def test_magic_quotes_runtime():
    expected = vuln('magic_quotes_runtime', '1', '0')
    assert expected in bad


def test_magic_quotes_sybase():
    expected = vuln('magic_quotes_sybase', '1', '0')
    assert expected in bad


def test_max_execution_time():
    expected = vuln('max_execution_time', '100', '30')
    assert expected in bad


def test_max_input_nesting_level():
    expected = vuln('max_input_nesting_level', '128', '64')
    assert expected in bad


def test_max_input_time():
    expected = vuln('max_input_time', '60', '30')
    assert expected in bad


def test_memory_limit():
    expected = vuln('memory_limit', '2G', '128M')
    assert expected in bad


def test_open_basedir():
    expected = vuln('open_basedir', '', 'some/path')
    assert expected in bad


def test_post_max_size():
    expected = vuln('post_max_size', '2G', '8M')
    assert expected in bad


def test_register_globals():
    expected = vuln('register_globals', '1', '0')
    assert expected in bad


def test_request_order():
    expected = vuln('request_order', '"PG"', 'GP')
    assert expected in bad


def test_safe_mode():
    expected = vuln('safe_mode', '0', '1')
    assert expected in bad


def test_session_cookie_httponly():
    expected = vuln('session.cookie_httponly', '0', '1')
    assert expected in bad


def test_session_cookie_lifetime():
    expected = vuln('session.cookie_lifetime', '60', '0')
    assert expected in bad


def test_session_cookie_secure():
    expected = vuln('session.cookie_secure', '0', '1')
    assert expected in bad


def test_session_save_path():
    expected = vuln('session.save_path', '"/tmp"', 'some/path')
    assert expected in bad


def test_session_use_cookies():
    expected = vuln('session.use_cookies', '0', '1')
    assert expected in bad


def test_session_use_only_cookies():
    expected = vuln('session.use_only_cookies', '0', '1')
    assert expected in bad


def test_use_strict_mode():
    expected = vuln('session.use_strict_mode', '0', '1')
    assert expected in bad


def test_upload_max_filesize():
    expected = vuln('upload_max_filesize', '2G', '2M')
    assert expected in bad


def test_missing_allow_url_fopen():
    expected = vuln('allow_url_fopen', 'not set', '0')
    assert expected in missing


def test_missing_assert_active():
    expected = vuln('assert.active', 'not set', '0')
    assert expected in missing


def test_missing_cgi_fix_pathinfo():
    expected = vuln('cgi.fix_pathinfo', 'not set', '0')
    assert expected in missing


def test_missing_disable_functions_popen():
    expected = vuln('disable_functions', 'not set',
                    'popen, exec, system, passthru, proc_open, shell_exec, apache_setenv, putenv, dl, expect_popen, pcntl_exec')
    assert expected in missing


def test_missing_display_errors():
    expected = vuln('display_errors', 'not set', '0')
    assert expected in missing


def test_missing_enable_dl():
    expected = vuln('enable_dl', 'not set', '0')
    assert expected in missing


def test_missing_expose_php():
    expected = vuln('expose_php', 'not set', '0')
    assert expected in missing


def test_missing_log_errors():
    expected = vuln('log_errors', 'not set', '1')
    assert expected in missing


def test_missing_open_basedir():
    expected = vuln('open_basedir', 'not set', 'some/path')
    assert expected in missing


def test_missing_magic_quotes_gpc():
    expected = vuln('magic_quotes_gpc', 'not set', '0')
    assert expected in missing


def test_missing_max_input_time():
    expected = vuln('max_input_time', 'not set', '30')
    assert expected in missing


def test_missing_safe_mode():
    expected = vuln('safe_mode', 'not set', '1')
    assert expected in missing


def test_missing_session_cookie_httponly():
    expected = vuln('session.cookie_httponly', 'not set', '1')
    assert expected in missing


def test_missing_session_cookie_secure():
    expected = vuln('session.cookie_secure', 'not set', '1')
    assert expected in missing


def test_missing_session_save_path():
    expected = vuln('session.save_path', 'not set', 'some/path')
    assert expected in missing


def test_missing_session_use_strict_mode():
    expected = vuln('session.use_strict_mode', 'not set', '1')
    assert expected in missing
