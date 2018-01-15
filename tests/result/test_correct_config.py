import os
from .run import run
import pytest

xfail = pytest.mark.xfail
path = os.path.realpath(os.path.join(os.path.dirname(__file__), 'correct'))
vulns = run(path)


def test_fp():
    assert len(vulns) == 0
