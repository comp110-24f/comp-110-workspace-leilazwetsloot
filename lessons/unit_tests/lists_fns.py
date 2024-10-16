"""testing class functions"""


def get_first(input: list[str]) -> str:
    """returns first elem in list"""
    return input[0]


def remove_first(input: list[str]) -> None:
    """removes(pop) the first elem in list"""
    input.pop(0)  # expects index argument (int)


def get_and_remove_first(input: list[str]) -> str:
    """takes first elem, prints and then removes it"""
    first: str = input[0]
    input.pop(0)
    return first
