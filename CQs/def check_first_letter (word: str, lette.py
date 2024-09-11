def check_first_letter(word: str, letter: str) -> str:
    """Checking to see if first letter of word matches"""
    if letter == word[0]:
        return "match!"
    else:
        return "no match!"
