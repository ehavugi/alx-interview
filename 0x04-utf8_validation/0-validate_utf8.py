#!/usr/bin/python3
"""
The utf-8 validation module.
Functions in clude validUTF8
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """return True if data is utf-8 otherwise False
    >>> validUTF8([120])
    True
    >>> validUTF8([229, 65, 127, 256])
    False
    >>> validUTF8([0, 100, 50,30])
    True
    >>> validUTF8([280])
    False
    """
    state = True
    skip = 0
    for index, value in enumerate(data):
        binary = "{0:b}".format(value)
        if len(binary) > 8:
            binary = binary[-8:]
        if value <= 127 and skip == 0:
            pass
        elif skip > 0:
            if binary[0:2] == '10':
                skip -= 1
            else:
                state = False
                break
        elif binary[0:3] == '110':
            skip = 1
        elif binary[0:4] == '1110':
            skip = 2
        elif binary[0:4] == '1111':
            skip = 3
        else:
            state = False

    if skip > 0:
        return False

    return state


if __name__ == "__main__":
    import doctest
    doctest.testmod()
