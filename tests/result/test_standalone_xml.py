import os
from .run import run, vuln
import pytest

xfail = pytest.mark.xfail

b, m = os.path.realpath(os.path.join(os.path.dirname(__file__), 'input_bad/standalone.xml')), os.path.realpath(
        os.path.join(os.path.dirname(__file__), 'input_missing/standalone.xml'))
bad, missing = run(b), run(m)


def test_fp():
    assert len(bad) == 5
    assert len(missing) == 4


def test_value():
    expected = vuln('@value', 'true', 'false')
    assert expected in bad


def test_default_user():
    expected = vuln('@default-user', '$local', '""')
    assert expected in bad


def test_scan_interval():
    expected = vuln('@scan-interval', '5000', '-1')
    assert expected in bad


def test_x_powered_by():
    expected = vuln('@x-powered-by', 'true', 'false')
    assert expected in bad


def test_display_source_fragment():
    expected = vuln('@display-source-fragment', 'true', 'false')
    assert expected in bad


def test_missing_default_user():
    expected = vuln('@default-user', 'not set', '""')
    assert expected in missing


def test_missing_scan_interval():
    expected = vuln('@scan-interval', 'not set', '-1')
    assert expected in missing


def test_missing_x_powered_by():
    expected = vuln('@x-powered-by', 'not set', 'false')
    assert expected in missing


def test_missing_display_source_fragment():
    expected = vuln('@display-source-fragment', 'not set', 'false')
    assert expected in missing
