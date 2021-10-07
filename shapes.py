import math
import turtle

X_MAX = 200
X_MIN = -200
Y_MAX = 200
Y_MIN = -200


def rectangle_will_fit(x, y, length, height):
    """
    function employed in checking if a rectangle can be drawn inside the window or not
    :param x: x coordinate
    :param y: y coordinate
    :param length: length of rectangle
    :param height: height of rectangle
    :return: True if fits, otherwise False
    """
    return x + length <= X_MAX and y + height <= Y_MAX


def circle_will_fit(x, y, radius):
    """
    function employed in checking if circle can be drawn inside the window or not
    :param x: x coordinate
    :param y: y coordinate
    :param radius: radius of circle
    :return: True if fits, otherwise False
    """
    diameter = 2 * radius
    return x + radius <= X_MAX and y + diameter <= Y_MAX


def triangle_will_fit(x, y, length):
    """
    function employed in checking if triangle will fit inside turtle window or not
    :param x: x coordinate
    :param y: y coordinate
    :param length: height of triangle
    :return: True if fits, otherwise False
    """
    height_y = (math.sqrt(3) * length) / 2
    return x + length <= X_MAX and y + height_y <= Y_MAX


def draw_shape(shape, color_code, x, y, length, height=0):
    """
    function employed in drawing figures
    r = rectangle
    c = circle
    t = triangle
    any other shape will draw nothing
    :return: None
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    perimeter = 0

    if shape == "r":
        if rectangle_will_fit(x, y, length, height):
            turtle.fillcolor(color_code)
            turtle.begin_fill()

            # drawing rectangle
            for i in range(4):
                if i % 2 == 0:  # drawing length of rectangle
                    turtle.forward(length)
                else:  # drawing height of rectangle
                    turtle.forward(height)
                turtle.left(90)
            turtle.end_fill()

            # calculating perimeter
            perimeter = 2 * (length + height)

    elif shape == "c":  # drawing circle
        if circle_will_fit(x, y, length):
            turtle.fillcolor(color_code)
            turtle.begin_fill()
            turtle.circle(length)
            turtle.end_fill()

            # calculating perimeter
            perimeter = 2 * math.pi * length

    elif shape == "t":  # drawing triangle
        if triangle_will_fit(x, y, length):
            turtle.fillcolor(color_code)
            turtle.begin_fill()
            for i in range(3):
                turtle.forward(length)
                turtle.left(120)
            turtle.end_fill()

            # calculating perimeter
            perimeter = 3 * length

    # setting turtle at start position
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # returning required details (perimeter, color, xcor, ycor)
    return perimeter, turtle.color()[1], turtle.xcor(), turtle.ycor()
