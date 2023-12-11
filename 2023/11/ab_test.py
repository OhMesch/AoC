import a
# import b

import pytest
@pytest.mark.parametrize("m, expected", [(a, 374)])

def test_a_solution_generation(m, expected):
    assert m.generateSolution("ab_test.dat") == expected