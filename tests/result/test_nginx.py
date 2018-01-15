import os
import pytest
from .run import run, vuln

xfail = pytest.mark.xfail

b, m, c = os.path.realpath(os.path.join(os.path.dirname(__file__), 'input_bad/nginx.conf')), os.path.realpath(
    os.path.join(os.path.dirname(__file__), 'input_missing/nginx.conf')), os.path.realpath(
    os.path.join(os.path.dirname(__file__), 'composite/nginx.conf'))

bad, missing, composite = run(b), run(m), run(c)

def test_fp():
    assert len(bad) == 10
    assert len(missing) == 8


def test_autoindex():
    expected = vuln('autoindex', 'on', 'off')
    assert expected in bad


def test_server_tokens():
    expected = vuln('server_tokens', 'on', 'off')
    assert expected in bad


def test_ssi():
    expected = vuln('ssi', 'on', 'off')
    assert expected in bad


def test_ssl_prefer_server_ciphers():
    expected = vuln('ssl_prefer_server_ciphers', 'off', 'on')
    assert expected in bad


def test_ssl_stapling():
    expected = vuln('ssl_stapling', 'off', 'on')
    assert expected in bad


def test_ssl():
    expected = vuln('ssl', 'off', 'on')
    assert expected in bad


def test_ssl_session_timeout():
    expected = vuln('ssl_session_timeout', '24h', '5m')
    assert expected in bad


def test_ssl_session_cache():
    expected = vuln('ssl_session_cache', 'builtin:2m', 'shared:SSL:2m')
    assert expected in bad


def test_ssl_protocols():
    expected = vuln('ssl_protocols', 'SSLv3', 'TLSv1 TLSv1.1 TLSv1.2')
    assert expected in bad


def test_ssl_ciphers_level():
    expected = vuln('ssl_ciphers', 'MEDIUM:aNULL:eNULL:EXPORT:DES:MD5:PSK:RC4',
                    'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH')
    assert expected in bad


def test_missing_ssl_prefer_server_ciphers():
    expected = vuln('ssl_prefer_server_ciphers', 'not set', 'on')
    assert expected in missing


def test_missing_ssl_stapling():
    expected = vuln('ssl_stapling', 'not set', 'on')
    assert expected in missing


def test_missing_ssl():
    expected = vuln('ssl', 'not set', 'on')
    assert expected in missing


def test_missing_ssl_certificate():
    expected = vuln('ssl_certificate', 'not set', 'path/to/cert')
    assert expected in missing


def test_missing_ssl_certificate_key():
    expected = vuln('ssl_certificate_key', 'not set', 'path/to/key')
    assert expected in missing


def test_missing_ssl_dhparam():
    expected = vuln('ssl_dhparam', 'not set', 'Path/to/dhparam')
    assert expected in composite


def test_missing_ssl_session_caches():
    expected = vuln('ssl_session_cache', 'not set', 'shared:SSL:2m')
    assert expected in missing


def test_missing_ssl_ciphers_1():
    expected = vuln('ssl_ciphers', 'not set', 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH')
    assert expected in missing
