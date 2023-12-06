import a
import b

import pytest
# @pytest.mark.parametrize("m, expected", [(a, 35), (b, 46)])

# def test_solution_generation(m, expected):
#     assert m.generateSolution("ab_test.dat") == expected

def test_combine_maps():
    m1 = [(3, 4, 10), (19, 30, 13)]
    m2 = [(15, 7, 10), (23, 25, 15)]
    expected = [(3, 1, 2), (15, 3, 8), (20, 10, 5), (18, 25, 5), (16, 30, 5), (16, 35, 5)]
    my_map = sorted(b.combine_maps(m1, m2), key=lambda x: x[1])
    print(f"{my_map=}")
    for i in range(50):
        print(i)
        assert a.map_lookup(m2, a.map_lookup(m1, i)) == b.map_lookup(my_map, i)
    