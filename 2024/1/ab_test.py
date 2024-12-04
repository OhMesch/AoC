import a
import b

def test_part_a_solution_generation():
    a_example_solution = 11
    assert a.generateSolution("ab_test.dat") == a_example_solution

def test_part_b_solution_generation():
    b_example_solution = 31
    assert b.generateSolution("ab_test.dat") == b_example_solution