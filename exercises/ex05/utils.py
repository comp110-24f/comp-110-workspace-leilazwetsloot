"""Implementing more list functions"""

__author__ = "730776566"

# a: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]


def only_evens(input: list[int]) -> list[int]:
    """returns only the even numbers from a list of integers"""
    evens: list[int] = []
    for num in input:
        if num % 2 == 0:
            evens.append(num)
    return evens


def sub(input: list[int], start: int, end: int) -> list[int]:
    """creates a subset of the given list between the given start and end index"""
    sub: list[int] = []
    fstart: int = start
    fend: int = end
    if start < 0:
        fstart = 0
    if end >= len(input):  # originally elif, but wrong
        fend = len(input)
    for index in range(fstart, fend):
        sub.append(input[index])
    return sub


def add_at_index(input: list[int], add: int, index: int) -> None:
    """modify the input list with the desired element at the given index"""
    if index > len(input) or index < 0:
        raise IndexError("Index is out of bounds for the input list")
    input.append(0)
    for spot in range(len(input) - 1, index, -1):
        input[spot] = input[spot - 1]
    input[index] = add
