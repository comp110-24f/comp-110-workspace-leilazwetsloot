"""File to define Bear class."""

__author__ = "730776566"


class Bear:
    """Bear class that has two attributes, age and hunger."""

    age: int
    hunger_score: int

    def __init__(self):
        """Intializes an object of the Bear class."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Creates the effect of one day on the bear."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Function shows how eating affects each bear object."""
        self.hunger_score += num_fish
