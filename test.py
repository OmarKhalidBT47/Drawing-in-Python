import math
import turtle
import pytest
from shapes import *


def test_draw_shape_rectangle():
    turtle.screensize(X_MAX, Y_MAX)
    turtle.tracer(0)
    x = draw_shape("r", "red", 0, 0, 50, 50)
    assert x[0] == 2 * (50 + 50)
    assert x[1] == "red"
    assert x[2] == 0
    assert x[3] == 0


def test_draw_shape_circle():
    turtle.screensize(X_MAX, Y_MAX)
    turtle.tracer(0)
    x = draw_shape("c", "green", 100, 100, 60)
    assert x[0] == 2 * math.pi * 60  # perimeter of circle
    assert x[1] == "green"
    assert x[2] == 100
    assert x[3] == 100


def test_draw_shape_triangle():
    turtle.screensize(X_MAX, Y_MAX)
    turtle.tracer(0)
    x = draw_shape("t", "blue", -100, 200, 70)
    assert x[0] == 3 * 70  # perimeter of triangle
    assert x[1] == "blue"
    assert x[2] == -100
    assert x[3] == 200


def test_rectangle_will_fit():
    x = rectangle_will_fit(0, 10, 50, 10)  # fit
    y = rectangle_will_fit(390, 390, 12, 12)  # not fit
    assert x == True
    assert y == False


def test_circle_will_fit():
    x = circle_will_fit(100, 100, 100)  # fit
    y = circle_will_fit(100, 100, 300)  # not fit
    assert x == True
    assert y == False


def test_triangle_will_fit():
    x = triangle_will_fit(100, 100, 100)  # fit
    y = triangle_will_fit(380, 100, 50)   # not fit
    assert x == True
    assert y == False
