import a
import b

import pytest

@pytest.mark.parametrize("m, expected", [(a, 136), (b, 64)])
def test_example(m, expected):
    assert m.generateSolution("ab_test.dat") == expected