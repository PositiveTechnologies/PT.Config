import os
from .run import run, vuln
import pytest

xfail = pytest.mark.xfail

b, m = os.path.realpath(os.path.join(os.path.dirname(__file__), 'user_rules/bad')), os.path.realpath(
        os.path.join(os.path.dirname(__file__), 'user_rules/missing'))
user_rules = os.path.join(os.path.dirname(__file__), 'user_rules/user_rules_example.js')
bad, missing = run(b, user_rules=user_rules), run(m, user_rules=user_rules)


def test_fp():
    assert len(bad) == 1
    assert len(missing) == 1


def test_user_defined_bad_option():
    expected = vuln('UserDefinedBadOption', 'Foo', 'Bar')
    assert expected in bad


def test_user_defined_missing_option():
    expected = vuln('UserDefinedMissingOption', 'not set', 'Bar')
    assert expected in missing
