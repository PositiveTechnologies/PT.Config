import os
from .run import run, vuln
import pytest

xfail = pytest.mark.xfail

b, m, c = os.path.realpath(os.path.join(os.path.dirname(__file__), 'input_bad/web.config')), os.path.realpath(
        os.path.join(os.path.dirname(__file__), 'input_missing/web.config')), os.path.realpath(
        os.path.join(os.path.dirname(__file__), 'composite/web.config'))

bad, missing, composite = run(b), run(m), run(c)


def test_fp():
    assert len(bad) == 37
    assert len(missing) == 25
    assert len(composite) == 5


def test_debug():
    expected = vuln('@debug', 'true', 'false')
    assert expected in bad


def test_mode():
    expected = vuln('@mode', 'Off', 'RemoteOnly')
    assert expected in bad


def test_enable_header_checking():
    expected = vuln('@enableHeaderChecking', 'false', 'true')
    assert expected in bad


def test_enable_view_state_mac():
    expected = vuln('@enableViewStateMac', 'false', 'true')
    assert expected in bad


def test_http_only_cookies():
    expected = vuln('@httpOnlyCookies', 'false', 'true')
    assert expected in bad


def test_require_ssl():
    expected = vuln('@requireSSL', 'false', 'true')
    assert expected in bad


def test_use_unsafe_header_parsing():
    expected = vuln('@useUnsafeHeaderParsing', 'true', 'false')
    assert expected in bad


def test_validate_request():
    expected = vuln('@validateRequest', 'false', 'true')
    assert expected in bad


def test_value():
    expected = vuln('@value', 'storage=file;deleteAfterServicing=false;', 'deleteAfterServicing=true;')
    assert expected in bad


def test_enabled():
    expected = vuln('@enabled', 'true', 'false')
    assert expected in bad


def test_maxRequestLength():
    expected = vuln('@maxRequestLength', '8192', '4096')
    assert expected in bad


def test_protection():
    expected = vuln('@protection', 'None', 'All')
    assert expected in bad


def test_credentials():
    expected = vuln('@name', 'admin', 'do not use')
    assert expected in bad


def test_identity_username():
    expected = vuln('@userName', 'admin', 'encrypted data')
    assert expected in bad


def test_slidingExpiration():
    expected = vuln('@slidingExpiration', 'true', 'false')
    assert expected in bad


def test_forms_requireSSL():
    expected = vuln('@requireSSL', 'false', 'true')
    assert expected in bad


def test_passwordFormat():
    expected = vuln('@passwordFormat', 'Clear', 'Hashed')
    assert expected in bad


def test_composite_timeout():
    expected = vuln('@timeout', '2880', '30')
    assert expected in composite


def test_composite_cookieTimeout():
    expected = vuln('@cookieTimeout', '50', '15')
    assert expected in composite


def test_composite_missing_cookieTimeout():
    expected = vuln('@cookieTimeout', 'not set', '15')
    assert expected in composite


def test_composite_level():
    expected = vuln('@level', 'Full', 'Medium')
    assert expected in composite


def test_composite_missing_level():
    expected = vuln('@level', 'not set', 'Medium')
    assert expected in composite


def test_connectionProtection():
    expected = vuln('@connectionProtection', 'None', 'Secure')
    assert expected in bad


def test_cookieProtection():
    expected = vuln('@cookieProtection', 'Encryption', 'All')
    assert expected in bad


def test_cookieRequireSSL():
    expected = vuln('@cookieRequireSSL', 'false', 'true')
    assert expected in bad


def test_cookieSlidingExpiration():
    expected = vuln('@cookieSlidingExpiration', 'true', 'false')
    assert expected in bad


def test_createPersistentCookie():
    expected = vuln('@createPersistentCookie', 'true', 'false')
    assert expected in bad


def test_validation():
    expected = vuln('@validation', 'MD5', 'SHA1')
    assert expected in bad


def test_validationKey():
    expected = vuln('@validationKey', '1234', 'AutoGenerate,IsolateApps')
    assert expected in bad

def test_decryptionKey():
    expected = vuln('@decryptionKey', '4321', 'AutoGenerate,IsolateApps')
    assert expected in bad


def test_allowOverride():
    expected = vuln('@allowOverride', 'true', 'false')
    assert expected in bad


def test_maxEventLengthForSimpleMessage():
    expected = vuln('@maxEventLengthForSimpleMessage', '10000', '5000')
    assert expected in bad


def test_maxSizeForSimpleMessage():
    expected = vuln('@maxSizeForSimpleMessage', '2048', '1024')
    assert expected in bad


def test_maxEventDetailLength():
    expected = vuln('@maxEventDetailLength', '10000', '5000')
    assert expected in bad


def test_minRequiredPasswordLength():
    expected = vuln('@minRequiredPasswordLength', '1', '7')
    assert expected in bad


def test_minRequiredNonalphanumericCharacters():
    expected = vuln('@minRequiredNonalphanumericCharacters', '0', '1')
    assert expected in bad


def test_AccessControlAllowOriginHeader():
    expected = vuln('@value', '*', '""')
    assert expected in bad


def test_enableVersionHeader():
    expected = vuln('@enableVersionHeader', 'true', 'false')
    assert expected in bad


def test_enableEventValidation():
    expected = vuln('@enableEventValidation', 'false', 'true')
    assert expected in bad


def test_viewStateEncryptionMode():
    expected = vuln('@viewStateEncryptionMode', 'Never', 'Always')
    assert expected in bad


def test_cookieless():
    expected = vuln('@cookieless', 'UseDeviceProfile', 'UseCookies')
    assert expected in bad


def test_enableCrossAppRedirects():
    expected = vuln('@enableCrossAppRedirects', 'true', 'false')
    assert expected in bad


def test_missing_sessionState_CipherValue():
    expected = vuln('CipherValue', 'not set', 'encrypted data')
    assert expected in missing


def test_missing_allowOverride():
    expected = vuln('@allowOverride', 'not set', 'false')
    assert expected in missing


def test_missing_cookieRequireSSL():
    expected = vuln('@cookieRequireSSL', 'not set', 'true')
    assert expected in missing


def test_missing_cookieSlidingExpiration():
    expected = vuln('@cookieSlidingExpiration', 'not set', 'false')
    assert expected in missing


def test_missing_slidingExpiration():
    expected = vuln('@slidingExpiration', 'not set', 'false')
    assert expected in missing


def test_missing_forms_requireSSL():
    expected = vuln('@requireSSL', 'not set', 'true')
    assert expected in missing


def test_missing_users():
    expected = vuln('@users', 'not set', '?')
    assert expected in missing


def test_missing_enableVersionHeader():
    expected = vuln('@enableVersionHeader', 'not set', 'false')
    assert expected in missing


def test_missing_viewStateEncryptionMode():
    expected = vuln('@viewStateEncryptionMode', 'not set', 'Always')
    assert expected in missing


def test_missing_cookieless():
    expected = vuln('@cookieless', 'not set', 'UseCookies')
    assert expected in missing


def test_missing_http_only_cookies():
    expected = vuln('@httpOnlyCookies', 'not set', 'true')
    assert expected in missing


def test_missing_require_ssl():
    expected = vuln('@requireSSL', 'not set', 'true')
    assert expected in missing


def test_error_code_400():
    expected = vuln('@statusCode', 'not set', '400')
    assert expected in missing


def test_error_code_401():
    expected = vuln('@statusCode', 'not set', '401')
    assert expected in missing


def test_error_code_403():
    expected = vuln('@statusCode', 'not set', '403')
    assert expected in missing


def test_error_code_404():
    expected = vuln('@statusCode', 'not set', '404')
    assert expected in missing


def test_error_code_405():
    expected = vuln('@statusCode', 'not set', '405')
    assert expected in missing


def test_error_code_408():
    expected = vuln('@statusCode', 'not set', '408')
    assert expected in missing


def test_error_code_411():
    expected = vuln('@statusCode', 'not set', '411')
    assert expected in missing


def test_error_code_413():
    expected = vuln('@statusCode', 'not set', '413')
    assert expected in missing


def test_error_code_414():
    expected = vuln('@statusCode', 'not set', '414')
    assert expected in missing


def test_error_code_500():
    expected = vuln('@statusCode', 'not set', '500')
    assert expected in missing


def test_error_code_502():
    expected = vuln('@statusCode', 'not set', '502')
    assert expected in missing


def test_error_code_503():
    expected = vuln('@statusCode', 'not set', '503')
    assert expected in missing


def test_error_code_504():
    expected = vuln('@statusCode', 'not set', '504')
    assert expected in missing
