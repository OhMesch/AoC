import a
import b

import pytest

def test_a_example():
    assert a.generateSolution("ab_test.dat", 6) == 16

def test_a_regression():
    assert a.generateSolution("ab.dat", 64) == 3658

@pytest.mark.parametrize("steps, expected", [
    (6, 16),
    (10, 50),
    (50, 1594),
    (100, 6536),
    (500, 167004),
    (1000, 668697),
    (5000, 16733044)
])
def test_b_example(steps, expected):
    assert b.generateSolution("ab_test.dat", steps) == expected

def test_b_regression():
    assert b.generateSolution("ab.dat") == 608193767979991