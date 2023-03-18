def dec_to_bin(value: int) -> list:
    parts = []

    while value != 0:
        parts.append(value % 2)
        value //= 2

    return parts[::-1]
