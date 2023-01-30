"""
Question 1

tl;dr Rewrite with `while` and make it go on **forever**

Hint: Remember to remove the parameter

This is function from Textbook Exercises #2 that draws a rectangular spiral.
Before, we only knew for loops, so we had to say what the max_side length was.

But now we know about `while` loops!

Make a new version of draw_rectangular_spiral that keeps spiralling outwards
until the program is closed.
"""

from turtle import *


####### EDIT THIS FUNCTION DECLARATION #######
# Remove the parameter `max_side`
def draw_rectangular_spiral(max_side):
    """Draw a rectangular spiral, starting in the center.
    
    `max_side` is the length of the longest side of the spiral in pixels"""
    
    ####### EDIT THIS FOR LOOP! #######
    # Rewrite with `while` and make it go on **forever**
    for side_length in range(1, max_side + 1, 5):
        forward(side_length)
        right(90)

####### EDIT THIS FUNCTION CALL #######
# Remove the argument
draw_rectangular_spiral(100)

