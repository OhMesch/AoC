import ab
import pytest


@pytest.mark.parametrize("smudges, expected", [(0, 405), (1, 400)])
def test_ab_example(smudges, expected):
    assert ab.generateSolution("ab_test.dat", smudges) == expected

@pytest.mark.parametrize("smudges, expected", [(0, 37561), (1, 31108)])
def test_ab_full(smudges, expected):
    assert ab.generateSolution("ab.dat", smudges) == expected