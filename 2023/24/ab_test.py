import a
import b

import pytest

def test_example():
    assert a.generateSolution("ab_test.dat", [7,27]) == 2

def test_b_example():
    assert b.generateSolution("ab_test.dat") == 47