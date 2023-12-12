import a
import b

import pytest

def test_a_regression():
    assert a.generateSolution("ab.dat") == 6981

# @pytest.mark.parametrize("m, expected", [(a, 21), (b,525152)])
# # @pytest.mark.parametrize("m, expected", [(a, 21)])
# def test_ab_solution_generation(m, expected):
#     assert m.generateSolution("ab_test.dat") == expected