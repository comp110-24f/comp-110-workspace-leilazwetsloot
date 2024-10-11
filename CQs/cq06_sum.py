"""Summing the elements of a list using different loops"""

__author__ = "730776566"


def w_sum(vals: list[float]) -> float:
    "returns the sum of the elemnets in a list using a while loop"
    index: int = 0
    sum: float = 0.0
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    "returns the sum of the elements in a list using a for in loop"
    sum: float = 0.0  # allows you to cut out index
    for nums in vals:
        sum += nums
    return sum


def f_range_sum(vals: list[float]) -> float:
    "returns the sum of the elements in a list using a range for in loop"
    sum: float = 0.0
    for index in range(0, len(vals)):
        sum += vals[index]
    return sum
