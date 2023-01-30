"""
Question 1

Rewrite the `draw_rectangular_spiral` function so that it draws a spiral that
goes on forever.

Hint: Remember to remove the parameter

This is function from Textbook Exercises #2 that draws a rectangular spiral.
Before, we only knew for loops, so we had to say what the max_side length was.

But now we know about `while` loops!
"""

from turtle import *

def draw_rectangular_spiral(max_side):
    """Draw a rectangular spiral, starting in the center.
    
    `max_side` is the length of the longest side of the spiral in pixels"""

    # Remember: When range takes 2 parameters, the first parameter is the start
    # and the second parameter is the end. So this range will start at 1 and
    # stop before it gets to max_side + 1 (i.e. it will stop at max_side)
    for side_length in range(1, max_side + 1, 5):
        forward(side_length)
        right(90)

draw_rectangular_spiral(100)