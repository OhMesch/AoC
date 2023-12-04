import a
import b

import pytest
@pytest.mark.parametrize("m, expected", [(a, 4361), (b, 467835)])

def test_solution_generation(m, expected):
    assert m.generateSolution("ab_test.dat") == expected
