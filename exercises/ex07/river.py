"""File to define River class."""

from exercises.ex07.bear import Bear
from exercises.ex07.fish import Fish

__author__ = "730776566"


class River:
    """Defining each object of a River."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks and handles the aging of all animals in the river."""
        young_fish: list[Fish] = []
        young_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                young_fish.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                young_bears.append(bear)
        self.fish = young_fish
        self.bears = young_bears
        return None

    def bears_eating(self):
        """Allows number to update as fish get eaten and decreases hunger_score."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def remove_fish(self, amount: int):
        """Removes fish from the river starting at the beginning of the list."""
        remove_times: int = 1
        while remove_times <= amount:
            self.fish.pop(0)
            remove_times += 1
        return None

    def check_hunger(self):
        """Checks that bears that died of starvation are removed accordingly."""
        not_starved_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                not_starved_bears.append(bear)  # same as check ages
        self.bears = not_starved_bears
        return None

    def repopulate_fish(self):
        """Handles repopulation of fish in pairs."""
        singles: int = len(self.fish)
        if singles % 2 == 1:
            singles -= 1
        couples: int = singles // 2
        n: int = 0
        while n < couples:
            self.fish.append(Fish())
            self.fish.append(Fish())
            self.fish.append(Fish())  # dang.
            self.fish.append(Fish())
            n += 1
        return None

    def repopulate_bears(self):
        """Handles repopulation of bears in pairs."""
        singles: int = len(self.bears)
        if singles % 2 == 1:  # "if odd"
            singles -= 1
        couples: int = singles // 2
        n: int = 0
        while n < couples:
            self.bears.append(Bear())
            n += 1
        return None

    def view_river(self):
        """Shows the river simulation interface."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")  # I LOVE f <3
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Shows one week worth of activity in the river."""
        while self.day <= 6:
            self.one_river_day()
