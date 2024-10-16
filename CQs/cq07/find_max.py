"""Practice with modifying lists"""

__author__ = "730776566"


def find_and_remove_max(input: list[int]) -> int:
    """determines and pops the largest number in a list"""
    if input == []:
        return -1  # the error return
    maxnum: int = input[0]
    for item in input:
        if item > maxnum:
            maxnum = item
    index: int = 0
    while index < len(input):
        if input[index] == maxnum:
            input.pop(
                index
            )  # when you pop at an index, the right most just takes its, place
            # so you cant auto add to index until it's false
        elif input[index] != maxnum:  # had to add line to make sure
            index += 1  # maybe too much code but I understand it
    return maxnum


c: list[int] = [1, 1, 1, 1, 1, 1]
print(find_and_remove_max(c))
print(c)
