'''
Task
Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.
'''

from math import sqrt


def is_square(num: int) -> bool:
    if num < 0:
        return False
    return sqrt(num).is_integer()
