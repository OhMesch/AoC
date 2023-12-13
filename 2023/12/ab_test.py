import a
import b
import c

import pytest

def test_a_regression():
    assert a.generateSolution("ab.dat") == 6981

@pytest.mark.parametrize("in_line, expected", [("????##???????##?#? 1,3,3,6", 9), (".?.????????##??? 1,1,7", 24), ("??????.???##??#?? 2,2,7", 14), ("??????.?.#?###? 1,1,1,1,6", 4)])
def test_c_bruteforce(in_line, expected):
    assert c.bruteForce(in_line) == expected

def test_c_scaled():
    assert c.generateSolution("ab_test.dat") == 21

def test_c_full():
    assert c.generateSolution("ab.dat") == 6981

@pytest.mark.parametrize("m, expected", [(a, 21), (b,525152), (c, 525152)])
def test_abc_solution_generation(m, expected):
    assert m.generateSolution("ab_test.dat") == expected