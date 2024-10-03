"""Mutating functions."""

__author__ = "730776566"

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(list: list[int], addition: int) -> None:
    """Manually adds an additional integer to the end of a list"""
    list.append(addition)  # will auto matically add to end


def double(list: list[int]) -> None:
    """Cycles through all values in list and multiplys by 2"""
    index: int = 0
    while index < len(list):  # length is the number of terms!
        list[index] *= 2  # can be shortened with operator
        index += 1


# I expect that it will update both list becasue the memory works dif with globals
