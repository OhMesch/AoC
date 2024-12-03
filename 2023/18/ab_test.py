import a
import b

import numpy as np

import pytest

@pytest.mark.parametrize("m, expected", [(a, 62), (b, 952408144115)])
def test_example(m, expected):
    assert m.generateSolution("ab_test.dat") == expected

def test_alcove():
    assert a.generateSolution("a_test.dat") == 258

def test_a_regression():
    assert a.generateSolution("ab.dat") == 74074

@pytest.mark.parametrize("filename, expected", [("b_test.dat", 700), ("b_test_2.dat", 62)])
def test_b_simple(filename, expected):
    assert b.generateSolution(filename) == expected

def test_b_gen_instructions():
    given_instructions = [
        ("0", 461937),
        ("1", 56407),
        ("0", 356671),
        ("1", 863240),
        ("0", 367720),
        ("1", 266681),
        ("2", 577262),
        ("3", 829975),
        ("2", 112010),
        ("1", 829975),
        ("2", 491645),
        ("3", 686074),
        ("2", 5411),
        ("3", 500254),
    ]
    assert b.parseInputFile("ab_test.dat") == given_instructions

def test_b_get_vert():
    instructions = [
        ("0", 10),
        ("1", 10),
        ("2", 10),
        ("3", 10)
    ]
    expected = [
        np.array([0, 0]),
        np.array([10, 0]),
        np.array([10, -10]),
        np.array([0, -10])
    ]
    for got, wanted in zip(b.generateDigVertices(instructions), expected):
        assert np.all(got == wanted)

@pytest.mark.parametrize("vert, area", [
    ([np.array([5,0]), np.array([5,5]), np.array([0,5]), np.array([0,0])], 25), 
    ([np.array([10,0]), np.array([5,5]), np.array([0,0])], 25),
    ([np.array([-5,0]), np.array([-5,5]), np.array([5,5]), np.array([5,0])], 50),
    ([np.array([-5,5]), np.array([-5,10]), np.array([20,10]), np.array([20,-30]), np.array([-10,-30]), np.array([-10,-15]), np.array([-20,-15]), np.array([-20,5])], 1375)
])
def test_b_area_calc(vert, area):
    assert b.calculatePolygonArea(vert) == area

@pytest.mark.parametrize("instructions, area", [
    ([("0", 10), ("1", 10), ("2", 10), ("3", 10)], 100),
    ([("0", 20), ("3", 20), ("0", 10), ("3", 10), ("2", 30), ("1", 30)], 700)
])
def test_b_gen_vert_and_calculate(instructions, area):
    dig_verts = b.generateDigVertices(instructions)
    assert b.calculatePolygonArea(dig_verts) == area