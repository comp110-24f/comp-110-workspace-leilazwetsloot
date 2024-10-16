"""Practice with testing functions"""

__author__ = "730776566"

from CQs.cq07.find_max import find_and_remove_max

a: list[int] = [1, 2, 3, 4, 5, 6]
b: list[int] = [1, 2, 3, 4, 3, 4, 2]
c: list[int] = [1, 1, 1, 1, 1]


def test_find_and_remove_max_return() -> None:
    """makes sure that correct max value is returned"""
    assert find_and_remove_max(a) == 6


def test_find_and_remove_max_mutate() -> None:
    """makes sure that list is mutated correctly"""
    find_and_remove_max(b)
    assert b == [1, 2, 3, 3, 2]


def test_find_and_remove_max_edge() -> None:
    """tests that a list of the same number will remove all"""
    find_and_remove_max(c)  # find out why error with keeping 1s around -> because auto
    # adding to index skips them
    assert c == []
