import math
import pytest
from components import Number, Vector, Point

def test_number_operations_and_repr():
    a = Number(3)
    b = Number(4)
    assert (a + b).value == 7
    assert (b - a).value == 1
    assert (a * b).value == 12
    assert (b / a).value == 4 / 3
    assert repr(a) == "Number(3)"


def test_vector_add_sub():
    dim = Number(3)
    v1 = Vector(dim, [Number(1), Number(2), Number(3)])
    v2 = Vector(dim, [Number(4), Number(5), Number(6)])
    v_sum = v1 + v2
    v_diff = v2 - v1
    assert isinstance(v_sum, Vector)
    assert [n.value for n in v_sum.values] == [5, 7, 9]
    assert [n.value for n in v_diff.values] == [3, 3, 3]


def test_vector_dot_and_scalar_multiplication():
    dim = Number(2)
    v1 = Vector(dim, [Number(1), Number(2)])
    v2 = Vector(dim, [Number(3), Number(4)])
    # dot product
    dot = v1 * v2
    assert isinstance(dot, Number)
    assert dot.value == 1 * 3 + 2 * 4
    # scalar multiplication (right and left)
    scalar = Number(2)
    v_scaled_r = v1 * scalar
    v_scaled_l = scalar * v1
    assert [n.value for n in v_scaled_r.values] == [2, 4]
    assert [n.value for n in v_scaled_l.values] == [2, 4]


def test_length_and_normalize():
    dim = Number(2)
    v = Vector(dim, [Number(3), Number(4)])
    length = v.length()
    assert isinstance(length, Number)
    assert math.isclose(length.value, 5.0)
    norm = v.normalize()
    assert isinstance(norm, Vector)
    assert pytest.approx([n.value for n in norm.values], rel=1e-9) == [3 / 5, 4 / 5]


def test_normalize_zero_vector_returns_notimplemented():
    dim = Number(3)
    zero = Vector(dim, [Number(0), Number(0), Number(0)])
    assert zero.normalize() is NotImplemented


def test_cross_product_3d_and_mismatch():
    dim3 = Number(3)
    i = Vector(dim3, [Number(1), Number(0), Number(0)])
    j = Vector(dim3, [Number(0), Number(1), Number(0)])
    k = i.cross(j)
    assert isinstance(k, Vector)
    assert [n.value for n in k.values] == [0, 0, 1]
    # dimension mismatch should return NotImplemented when calling method directly
    dim2 = Number(2)
    v2 = Vector(dim2, [Number(1), Number(2)])
    assert i.cross(v2) is NotImplemented


def test_point_equality_and_location_vector():
    p1 = Point(Number(2), [Number(1), Number(2)])
    p2 = Point(Number(2), [Number(1), Number(2)])
    p3 = Point(Number(2), [Number(2), Number(1)])
    assert p1 == p2
    assert not (p1 == p3)
    lv = p1.location_vector()
    assert isinstance(lv, Vector)
    assert [n.value for n in lv.values] == [1, 2]


def test_vector_add_dimension_mismatch_returns_notimplemented():
    v2 = Vector(Number(2), [Number(1), Number(2)])
    v3 = Vector(Number(3), [Number(1), Number(2), Number(3)])
    # operator would raise TypeError if NotImplemented is returned; test the special method directly
    assert v2.__add__(v3) is NotImplemented
    assert v2.__sub__(v3) is NotImplemented
    assert v2.__mul__(v3) is NotImplemented