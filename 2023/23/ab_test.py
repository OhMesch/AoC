import a
import b
import c

import pytest

@pytest.mark.parametrize("module, expected", [(a, 94), (b, 154), (c, 154)])
def test_example(module, expected):
    assert module.generateSolution("ab_test.dat") == expected

def test_c_graph():
    grid = c.parseInputFile("simple_graph.dat")
    graph = c.buildWeightedGraph(grid, (1,0), (len(grid[0])-2, len(grid)-1))
    c.printGraph(graph)
    assert c.longestSimplePath(graph) == 17

# def test_c_regression():
#     assert 6751 > c.generateSolution("ab.dat") > 4646