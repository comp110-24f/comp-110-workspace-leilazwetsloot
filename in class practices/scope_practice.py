def remove_chars(msg: str, char: str) -> str:  # type: ignore
    """Return a copy of a message with all char removed"""
    copy: str = ""  # an empty string where values are copied over
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy += msg[index]
        index += 1
    return copy


word: str = "yoyo"
