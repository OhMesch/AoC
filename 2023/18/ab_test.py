import a
# import b

import pytest

@pytest.mark.parametrize("m, expected", [(a, 62)])
def test_example(m, expected):
    assert m.generateSolution("ab_test.dat") == expected

def test_alcove():
    assert a.generateSolution("a_test.dat") == 258
    