#!/usr/bin/python3
def remove_char_at(str, n):
    """Generate a duplicate of the string excluding the character at index n"""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
