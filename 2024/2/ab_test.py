import a
import b

def test_part_a_solution_generation():
    a_example_solution = 2
    assert a.generateSolution("ab_test.dat") == a_example_solution

def test_part_a_wrong_solution_generation():
    wrong = 374
    assert a.generateSolution("ab.dat") != wrong

def test_part_b_solution_generation():
    b_example_solution = 4
    assert b.generateSolution("ab_test.dat") == b_example_solution

def test_part_b_wrong_solution_generation():
    wrong = 507
    assert b.generateSolution("ab.dat") != wrong