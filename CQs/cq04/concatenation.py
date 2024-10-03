"""Part of Challenge Question 04 - Importing and Scope"""

__author__ = "730776566"


def concat(inp1: str, inp2: str) -> str:
    """Returns the concatenation fo 2 strings"""
    return inp1 + inp2


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":  # this makes it so that the call doesnt run when imported
    print(concat(word1, word2))
