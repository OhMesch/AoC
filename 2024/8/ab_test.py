import a
import b

def test_part_a_solution_generation():
    a_example_solution = 1928
    assert a.generateSolution("ab_test.dat") == a_example_solution

def test_part_b_solution_generation():
    b_example_solution = 2858
    assert b.generateSolution("ab_test.dat") == b_example_solution

def test_part_b_2_solution_generation():
    b_example_solution = 2858
    assert b.generateSolution("ab_test2.dat") == b_example_solution