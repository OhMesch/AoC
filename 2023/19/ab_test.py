import a
import b

import math

import pytest

@pytest.mark.parametrize("m, expected", [(a, 19114), (b, 167409079868000)])
def test_example(m, expected):
    assert m.generateSolution("ab_test.dat") == expected

def test_b_range_generation():
    workflows = b.parseInputFile("ab_test.dat")
    possible_ranges = b.exploreWorkflow(workflows, 'in', 0, {'x': (1, 4001), 'm': (1, 4001), 'a': (1, 4001), 's': (1, 4001)})
    expected_ranges = [
        {'x': (1, 1416), 'm': (1, 4001), 'a': (1, 2006), 's': (1, 1351)},
        {'x': (2663, 4001), 'm': (1, 4001), 'a': (1, 2006), 's': (1, 1351)},
        {'x': (1, 4001), 'm': (2091, 4001), 'a': (2006, 4001), 's': (1, 1351)},
        {'x': (1, 2441), 'm': (1, 2091), 'a': (2006, 4001), 's': (537, 1351)},
        {'x': (1, 4001), 'm': (1, 4001), 'a': (1, 4001), 's': (3449, 4001)},
        {'x': (1, 4001), 'm': (1549, 4001), 'a': (1, 4001), 's': (2771, 3449)},
        {'x': (1, 4001), 'm': (1, 1549), 'a': (1, 4001), 's': (2771, 3449)},
        {'x': (1, 4001), 'm': (839, 1801), 'a': (1, 4001), 's': (1351, 2771)},
        {'x': (1, 4001), 'm': (1, 839), 'a': (1, 1717), 's': (1351, 2771)},
    ]
    running_sum = 0
    for p in expected_ranges:
        running_sum += math.prod([r[1]-r[0] for r in p.values()])
    assert running_sum == 167409079868000
    assert possible_ranges == expected_ranges