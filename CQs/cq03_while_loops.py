"""While Loops Challenge Question"""

__author__ = "730776566"


def num_instances(phrase: str, search_char: str) -> int:
    """Function determines how many times a character is present in a word"""
    count: int = 0
    index: int = 0
    while index < len(phrase):  # makes sure that it's only working within word
        if phrase[index] == search_char:  # 'if letter is equal to search char"
            count = count + 1  # add one to count
        index = index + 1  # and try next letter
    return count
