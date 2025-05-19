import a
import b

def test_part_a_solution_generation():
    a_example_solution = 55312
    assert a.generateSolution("ab_test.dat") == a_example_solution

def test_part_b_solution_generation():
    b_example_solution = 55312
    assert b.generateSolution("ab_test.dat") == b_example_solution

# def test_part_b_wrong():
#     low = 199753
#     assert b.generateSolution("ab_test.dat") > low