import a
# import b

import pytest

@pytest.mark.parametrize("m, expected", [(a, 32000000)])
def test_example_simple(m, expected):
    assert m.generateSolution("ab_test.dat") == expected

@pytest.mark.parametrize("m, expected", [(a, 11687500)])
def test_example(m, expected):
    assert m.generateSolution("ab_test_2.dat") == expected
