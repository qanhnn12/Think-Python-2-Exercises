import math
import turtle


# EXERCISE 4.3.1
# Write a function called square that takes a parameter named t, which is a turtle.
# Write a function call that passes bob as an argument to square, and run the program again.

def square_1(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)


"""
bob = turtle.Turtle()
square_1(bob)
"""


# EXERCISE 4.3.2
# Add another parameter, named length, to square.

def square_2(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


"""
bob = turtle.Turtle()
square_2(bob, 250)
"""


# EXERCISE 4.3.3
# Write a n-sided regular polygon by adding a parameter named n.
# Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.

def polygon_1(t, n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)


"""
bob = turtle.Turtle()
polygon_1(bob, 6, 80)
"""


# EXERCISE 4.3.4
# Write a circle, which takes a radius named r as a parameter.
# Hint: circumference = length * n (n is constant).


def circle_1(t, r):
    circumference = 2 * math.pi * r
    n = 60
    length = circumference / n
    polygon_1(t, n, length)


"""
bob = turtle.Turtle()
circle_1(bob, 90)
"""


# Rewrite the circle function so n is not constant value.

def circle_2(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3  # Adding 3 to n guarantees that the polygon has at least 3 sides.
    length = circumference / n
    polygon_1(t, n, length)


"""
bob = turtle.Turtle()
circle_2(bob, 75)
"""


# EXERCISE 4.3.5
# Write arc function that takes an additional parameter angle, which determines what fraction of a circle to draw
# copy of polygon and transform it into arc
def arc_1(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)


# rewrite polygon and arc to use polyline
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon_2(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)


def arc_2(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


def circle_3(t, r):
    arc_2(t, r, 360)


if __name__ == '__main__':
    bob = turtle.Turtle()
    circle_3(bob, 100)
