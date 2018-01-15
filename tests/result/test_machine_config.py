import os
from .run import run, vuln
import pytest

xfail = pytest.mark.xfail

b, m = os.path.realpath(os.path.join(os.path.dirname(__file__), 'input_bad/machine.config')), os.path.realpath(
        os.path.join(os.path.dirname(__file__), 'input_missing/machine.config'))
bad, missing = run(b), run(m)

def test_fp():
    assert len(bad) == 7
    assert len(missing) == 2


def test_passwordFormat():
    expected = vuln('@passwordFormat', 'MD5', 'SHA1')
    assert expected in bad


def test_retail():
    expected = vuln('@retail', 'false', 'true')
    assert expected in bad


def test_decryption():
    expected = vuln('@decryption', 'DES', 'Auto')
    assert expected in bad


def test_decryptionKey():
    expected = vuln('@decryptionKey', '123456789', 'AutoGenerate,IsolateApps')
    assert expected in bad


def test_validation():
    expected = vuln('@validation', 'HMACSHA256', 'AES')
    assert expected in bad


def test_validationKey():
    expected = vuln('@validationKey', '987654321', 'AutoGenerate,IsolateApps')
    assert expected in bad


def test_debug():
    expected = vuln('@debug', 'true', 'false')
    assert expected in bad


def test_missing_retail():
    expected = vuln('@retail', 'not set', 'true')
    assert expected in missing


def test_missing_validation():
    expected = vuln('@validation', 'not set', 'AES')
    assert expected in missing
