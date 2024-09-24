"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730776566"


def input_word() -> str:  # type: ignore #still recieving an error on type but it fine
    chosen_word: str = input("Enter a 5-character word: ")
    if len(chosen_word) != 5:  # had to remember operator
        print("Error: Word must contain 5 characters.")
        exit()
    elif len(chosen_word) == 5:
        return chosen_word


def input_letter() -> str:  # type: ignore
    chosen_letter: str = input("Enter a single character: ")
    if len(chosen_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    elif len(chosen_letter) == 1:
        return chosen_letter


def contains_char(word: str, letter: str) -> None:
    count: int = 0  # originally added to many variables
    print(
        "Searching for " + letter + " in " + word
    )  # had to redo entire ex because used while loop and didn't make sense
    if word[0] == letter:
        print(
            letter + " found at index 0"
        )  # had to go back and include spaces so they concatenated well
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1  # this was simple to figure out
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    if count > 1:
        print(str(count) + " instances of " + letter + " found in " + word)
    if count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    if count == 0:
        print("No instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(input_word(), input_letter())


if __name__ == "__main__":
    main()

main()
