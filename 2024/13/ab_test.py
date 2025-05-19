import a
import b

def test_part_a_solution_generation():
    a_example_solution = 480
    assert a.generateSolution("ab_test.dat") == a_example_solution

def test_part_b_solution_generation():
    b_example_solution = 480
    assert b.generateSolution("ab_test.dat") == b_example_solution

def test_part_b_high():
    high = 151472829754081
    assert b.generateSolution("ab.dat") < high

def test_part_b_low():
    low = 38839
    assert b.generateSolution("ab.dat") > low