"""Definining unit tests for utils.py"""

__author__ = "730776566"

from exercises.ex05.utils import only_evens, sub, add_at_index

import pytest

# lists to use
list1: list[int] = [1, 2, 3, 5]
a: list[int] = [1, 2, 3, 4]


def test_only_evens1() -> None:
    """makes sure that only_evens functions correctly"""
    assert only_evens(input=[1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_only_evens2() -> None:
    """makes sure that test_only_evens cycles through all indices correctly"""
    assert only_evens(input=[2, 2, 2, 2, 1]) == [2, 2, 2, 2]


def test_only_evens3() -> None:
    """checks that an empty list is returned from an empty input"""
    assert only_evens(input=[]) == []


def test_sub1() -> None:
    """tests that subset works normally"""
    assert sub(input=[1, 2, 3, 4, 5], start=1, end=4) == [2, 3, 4]


def test_sub2() -> None:
    """tests that sub correctly readjusts out of bounds indices"""
    assert sub(input=[2, 4, 6, 8], start=-2, end=10) == [2, 4, 6, 8]


def test_sub3() -> None:
    """Tests that sub returns a empty subset from an empty list"""
    assert sub(input=[], start=1, end=3) == []


def test_add_at_index1() -> None:
    """tests to make sure input list is correctly mutated"""
    add_at_index(input=a, add=5, index=4)
    assert a == [1, 2, 3, 4, 5]


def test_add_at_index_return() -> None:
    """tests to make sure input index out of range will return an error"""
    with pytest.raises(IndexError):
        add_at_index(input=a, add=5, index=10)


def test_add_at_index2() -> None:
    """Makes sure that extra 0 space isnt added to an empty list"""
    empty: list[int] = []
    add_at_index(input=empty, add=4, index=0)
    assert empty == [4]
