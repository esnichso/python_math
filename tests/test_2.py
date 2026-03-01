import math
import pytest
from components import Number, Vector, Matrix

def test_matrix_add():
    m1 = Matrix(Number(2), Number(2), [[Number(1), Number(2)], [Number(3), Number(4)]])
    m2 = Matrix(Number(2), Number(2), [[Number(5), Number(6)], [Number(7), Number(8)]])
    m_sum = m1 + m2
    assert isinstance(m_sum, Matrix)
    assert m_sum.rows.value == 2
    assert m_sum.columns.value == 2
    assert [[n.value for n in row] for row in m_sum.values] == [[6, 8], [10, 12]]


def test_matrix_sub():
    m1 = Matrix(Number(2), Number(2), [[Number(5), Number(6)], [Number(7), Number(8)]])
    m2 = Matrix(Number(2), Number(2), [[Number(1), Number(2)], [Number(3), Number(4)]])
    m_diff = m1 - m2
    assert isinstance(m_diff, Matrix)
    assert [[n.value for n in row] for row in m_diff.values] == [[4, 4], [4, 4]]


def test_matrix_mul_matrix():
    m1 = Matrix(Number(2), Number(3), [[Number(1), Number(2), Number(3)], [Number(4), Number(5), Number(6)]])
    m2 = Matrix(Number(3), Number(2), [[Number(7), Number(8)], [Number(9), Number(10)], [Number(11), Number(12)]])
    m_prod = m1 * m2
    assert isinstance(m_prod, Matrix)
    assert m_prod.rows.value == 2
    assert m_prod.columns.value == 2
    assert [[n.value for n in row] for row in m_prod.values] == [[58, 64], [139, 154]]


def test_matrix_mul_vector():
    m = Matrix(Number(2), Number(3), [[Number(1), Number(2), Number(3)], [Number(4), Number(5), Number(6)]])
    v = Vector(Number(3), [Number(1), Number(2), Number(3)])
    result = m * v
    assert isinstance(result, Vector)
    assert result.dimension.value == 2
    assert [n.value for n in result.values] == [14, 32]


def test_vector_mul_matrix():
    v = Vector(Number(2), [Number(1), Number(2)])
    m = Matrix(Number(2), Number(3), [[Number(1), Number(2), Number(3)], [Number(4), Number(5), Number(6)]])
    result = v * m
    assert isinstance(result, Vector)
    assert result.dimension.value == 3
    assert [n.value for n in result.values] == [9, 12, 15]


def test_matrix_add_dimension_mismatch_returns_notimplemented():
    m1 = Matrix(Number(2), Number(2), [[Number(1), Number(2)], [Number(3), Number(4)]])
    m2 = Matrix(Number(3), Number(3), [[Number(1), Number(2), Number(3)], [Number(4), Number(5), Number(6)], [Number(7), Number(8), Number(9)]])
    assert m1.__add__(m2) is NotImplemented


def test_matrix_mul_dimension_mismatch_returns_notimplemented():
    m1 = Matrix(Number(2), Number(2), [[Number(1), Number(2)], [Number(3), Number(4)]])
    m2 = Matrix(Number(3), Number(3), [[Number(1), Number(2), Number(3)], [Number(4), Number(5), Number(6)], [Number(7), Number(8), Number(9)]])
    assert m1.__mul__(m2) is NotImplemented


def test_matrix_vector_mul_dimension_mismatch_returns_notimplemented():
    m = Matrix(Number(2), Number(2), [[Number(1), Number(2)], [Number(3), Number(4)]])
    v = Vector(Number(3), [Number(1), Number(2), Number(3)])
    assert m.__mul__(v) is NotImplemented


def test_matrix_repr():
    m = Matrix(Number(2), Number(2), [[Number(1), Number(2)], [Number(3), Number(4)]])
    assert repr(m) == "2x2-Matrix([[Number(1), Number(2)], [Number(3), Number(4)]])"