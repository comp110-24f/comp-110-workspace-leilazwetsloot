"""Part of Challenge Question 04 - Importing and Scope"""

__author__ = "730776566"

from concatenation import concat  # originally included too many locations oops
from coordinates import get_coords  # error shown when not placed above global variables

x: str = "123"
y: str = "abc"
print(concat(x, y))
get_coords(x, y)  # runs yippeee
