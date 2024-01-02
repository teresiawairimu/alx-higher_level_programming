#!/usr/bin/python3

def islower(c):
    """The function verifies the presence of lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
