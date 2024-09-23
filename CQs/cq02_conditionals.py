"""Practice with Conditionals, Local Variables, and User Input"""

__author__ = "730776566"  # I need to be able to write this without looking it up


def guess_a_number() -> None:
    """Function for number guessing game!!!!!"""
    secret: int = 7
    x: str = input(
        "Guess a number:"
    )  # took a wee bit to understand I needed 2 local variables
    print(str("Your guess was ") + x)
    if int(x) == secret:
        print("You got it!")
    elif int(x) < secret:
        print(str("Your guess was too low! The secret number is ") + str(secret))
    elif int(x) > secret:
        print(str("Your guess was too high! The secret number is ") + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
