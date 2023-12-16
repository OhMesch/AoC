import a
import b

import pytest

@pytest.mark.parametrize("m, expected", [(a, 46), (b, 51)])
def test_example(m, expected):
    assert m.generateSolution("ab_test.dat") == expected