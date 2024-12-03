import a
import b

import pytest

@pytest.mark.parametrize("m, expected", [(a, 102), (b, 94)])
def test_example(m, expected):
    assert m.generateSolution("ab_test.dat") == expected

def test_b_example():
    assert b.generateSolution("b_test.dat") == 71

def test_b2_example():
    assert b.generateSolution("b_test_2.dat") == 44

def test_b_sol_on_a():
    assert b.generateSolution("ab.dat", (1,3)) == 1099