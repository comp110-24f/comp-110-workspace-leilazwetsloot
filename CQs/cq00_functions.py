"""Challenge Question 00"""

__author__ = "730776566"


def mimic(message: str) -> str:
    """Function that mimics input string"""
    return message


def main() -> None:
    """Only print the result of calling mimic"""
    print(mimic(message=input("What is your message? ")))


if __name__ == "__main__":
    main()
