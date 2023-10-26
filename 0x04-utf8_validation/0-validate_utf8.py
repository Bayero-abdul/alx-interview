#!/usr/bin/python3
"""0-validate_utf8.py. """


def validUTF8(data):
    """Validate if a given data set represent utf-8 encoding. """
    count = 0

    for byte in data:
        if count == 0:
            if byte & 0x80 == 0:
                count = 0
            elif byte & 0xE0 == 0xC0:
                count = 1
            elif byte & 0xF0 == 0xE0:
                count = 2
            elif byte & 0xF8 == 0xF0:
                count = 3
            else:
                return False
        else:
            if byte & 0xC0 == 0x80:
                count -= 1
            else:
                return False
    return count == 0
