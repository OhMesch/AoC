import a
import b

import pytest
@pytest.mark.parametrize("m, file, expected", [(a, "ab_test.dat", 8), (b, "ab_test_2.dat", 8), (b, "ab_test_3.dat", 10), (b, "ab_test_4.dat", 4)])

def test_a_solution_generation(m, file, expected):
    assert m.generateSolution(file) == expected