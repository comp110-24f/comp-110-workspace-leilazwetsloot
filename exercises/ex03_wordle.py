"""A exercise meant to mimic the game, Wordle"""

__author__ = "730776566"


def input_guess(
    secret_word_length: int,
) -> str:  # had help in tutoring to know return type
    """Allows user to input a guess word and checks it for validity"""
    guess: str = input(
        f"Enter a {secret_word_length} character word: "
    )  # had to work a bit to rewrite to an f-string
    while len(guess) != secret_word_length:  # loop until lengths are equal
        guess = input((f"That wasn't {secret_word_length} chars! Try again: "))
    return guess  # originally "print" but was casuing an assertion error within main


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Test each index of the secret word for the guessed character"""
    assert len(char_guess) == 1  # from example, assumes char_guess is 1 char long
    index: int = 0
    while index < len(secret_word):
        if (
            secret_word[index] == char_guess
        ):  # cut out a second if statement that was causing a block
            return True
        index += 1
    return False  # added in tutoring to work with emojified


def emojified(guess: str, secretword: str) -> str:
    """Colored emojis will be used to show wordle imaging"""
    assert len(guess) == len(secretword)
    index: int = 0
    copy: str = ""  # similar to inclass practice
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while index < len(secretword):
        if secretword[index] == guess[index]:
            copy += GREEN_BOX
        elif contains_char(
            secret_word=secretword, char_guess=guess[index]
        ):  # originally an if, changed to elif
            copy += YELLOW_BOX
        else:
            copy += WHITE_BOX
        index += 1
    return copy


def main(secret: str) -> None:
    """The entry point of the program and the main game loop."""
    turns: int = 1
    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(secret_word_length=len(secret))
        print(emojified(guess=guess, secretword=secret))
        if guess == secret:
            print(f"You won in {turns}/6 turns!")
            turns = 7  # arbitrary turn number to exit loop
        elif turns == 6:  # again, another elif
            print("X/6 - Sorry, try again tomorrow!")
        turns += 1


if __name__ == "__main__":
    main(secret="codes")
