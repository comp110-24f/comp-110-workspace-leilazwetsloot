"""Implementing Algorithims to promote computational thinking"""

__author__ = "730776566"


def all(list: list[int], num: int) -> bool:
    """Returns a bool indicating whether all of the ints in the list equal a number"""
    if len(list) == 0:
        return False
    for item in list:
        if item != num:
            return False  # can exit out of for in loop
    return True


def max(input: list[int]) -> int:
    """returns the highest quantitative number in a list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    maxnum: int = input[0]  # origially set at zero but what if negative num
    for item in input:
        if item >= maxnum:  # fixes issue with index 0
            maxnum = item
    return maxnum


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """compares the equality of two separate lists"""
    if (
        list1 == list2
    ):  # didnt think it would be this easy but lists work in mem i guess
        return True
    else:
        return False


def extend(list1: list[int], list2: list[int]) -> None:
    """Appends one list to the end of the first"""
    for item in list2:  # used to cycle through and add each from list two
        list1.append(item)
    print(list1)
