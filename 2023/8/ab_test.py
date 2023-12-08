import a
import b

import pytest
@pytest.mark.parametrize("m, data_file, expected", [(a, 'a_test_1.dat', 2), (a, 'a_test_2.dat', 6), (b, 'b_test.dat', 6)])

def test_solution_generation(m, data_file, expected):
    assert m.generateSolution(data_file) == expected