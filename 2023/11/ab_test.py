import ab
import graph

import pytest

@pytest.mark.parametrize("expansion, expected", [(2, 374), (10, 1030), (100, 8410)])
def test_a_solution_generation(expansion, expected):
    assert ab.generateSolution("ab_test.dat", expansion) == expected

@pytest.mark.parametrize("expansion, expected", [(2, 374), (10, 1030), (100, 8410)])
def test_b_solution_generation(expansion, expected):
    assert graph.generateSolution("ab_test.dat", expansion) == expected