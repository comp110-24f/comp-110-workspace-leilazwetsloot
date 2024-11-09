"""File to define Fish class."""

__author__ = "730776566"


class Fish:
    """Each fish object will have one attribute, age."""

    age: int

    def __init__(self):
        """Initializes each Fish object."""
        self.age = 0
        return None

    def one_day(self):
        """Creates the effects of aging on fish objects."""
        self.age += 1
        return None
