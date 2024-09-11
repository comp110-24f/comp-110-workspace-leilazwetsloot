"""Planning a tea party to practice functions!"""

__author__ = "730776566"


def main_planner(guests: int) -> None:
    """Main tea party planning function"""
    print(("A Cozy Tea Party for ") + str(guests) + (" People!"))
    tea_bag_number: int = tea_bags(
        people=guests
    )  # went to office hours to understand that I needed to add local variables to function
    treat_number: int = treats(people=guests)
    print(("Tea Bags: ") + str(tea_bag_number))
    print(("Treats: ") + str(treat_number))
    print(("Cost: $") + str(cost(tea_count=tea_bag_number, treat_count=treat_number)))
    return None


def tea_bags(people: int) -> int:
    """The number of teabags needed for guests"""
    return people * 2


def treats(people: int) -> int:
    """The number of treats need for guests"""
    return int(1.5 * tea_bags(people=people))  # overheard this while leaving lecture!


def cost(tea_count: int, treat_count: int) -> float:
    """Computing the cost of the tea bags and treats combined"""
    return float(
        tea_count * 0.50 + treat_count * 0.75
    )  # unrelated to tea bags and treats counters in original function def


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
