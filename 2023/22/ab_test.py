import a
import b

import pytest

@pytest.mark.parametrize("module, expected", [(a, 5), (b, 7)])
def test_example(module, expected):
    assert module.generateSolution("ab_test.dat") == expected

# def test_b_custom():
#     assert b.generateSolution("ab_example.dat") == 10

# def test_b_mega_short():
#     assert b.generateSolution("ab_mega_short.dat") == 40

def test_a_short():
    assert a.generateSolution("ab_short.dat") == 40

def test_a_regression():
    assert a.generateSolution("ab.dat") == 475
    
def test_b_regression():
    assert b.generateSolution("ab.dat") > 42566
