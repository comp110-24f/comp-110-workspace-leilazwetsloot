"""Exercise 06 to get practice with dictionary functions"""

__author__ = "730776566"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of the input dictionary"""
    return_dict: dict[str, str] = {}
    for key in input:  # cycles through each key
        if (
            input[key] not in return_dict
        ):  # if the value has not been alr turned into a key...
            return_dict[input[key]] = key
        else:
            raise KeyError("Inverting will create duplicate keys.")
    return return_dict


def favorite_color(colors: dict[str, str]) -> str:
    """returns the mot frequent color from all listed"""
    just_colors: dict[str, int] = {}
    for person in colors:
        if colors[person] not in just_colors:
            just_colors[colors[person]] = 0
        else:
            just_colors[colors[person]] += 1
    favcolor: str = ""
    max: int = 0
    for color in just_colors:
        if just_colors[color] > max:
            max = just_colors[color]
    for color in just_colors:
        if just_colors[color] == max:
            favcolor = color
    return favcolor  # this definitely feels way more complicated than it needs to be

    # print(
    favorite_color(
        {
            "Marc": "yellow",
            "Ezri": "blue",
            "kris": "blue",
            "jamie": "green",
            "jackie": "green",
            "lola": "green",
        }
    )


def count(inputlist: list[str]) -> dict[str, int]:
    """creates a dictionary that tracks the frequencies of numbers"""
    numfreq: dict[str, int] = {}
    for num in inputlist:
        if num in numfreq:
            numfreq[num] += 1
        if num not in numfreq:
            numfreq[num] = 1
    return numfreq  # figured it out i had the input list type wrong


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """returns a dict with the key as the first letter of the word"""
    returndict: dict[str, list[str]] = {}
    for word in input:
        if word[0].lower() not in returndict:  # lower helps a lot
            returndict[word[0].lower()] = [word]
        elif word[0].lower() in returndict:
            returndict[word[0].lower()] += [word]
    return returndict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """mutates an attendence log dictionary"""
    if day not in attendance:
        attendance[day] = [student]
    elif day in attendance:
        if attendance[day] != [student]:  # ensures name isn't added twice
            attendance[day] += [student]
