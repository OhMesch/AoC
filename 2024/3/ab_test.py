import a
import b

def test_part_a_solution_generation():
    a_example_solution = 161
    assert a.generateSolution("a_test.dat") == a_example_solution

def test_part_b_solution_generation():
    b_example_solution = 48
    assert b.generateSolution("b_test.dat") == b_example_solution

def test_part_b_wrong_solution_generation():
    b_example_solution = 127870505
    assert b.generateSolution("ab.dat") < b_example_solution