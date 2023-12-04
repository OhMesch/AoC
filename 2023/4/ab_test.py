import a
import b

import pytest
@pytest.mark.parametrize("m, expected", [(a, 13), (b, 30)])

def test_solution_generation(m, expected):
    assert m.generateSolution("ab_test.dat") == expected
