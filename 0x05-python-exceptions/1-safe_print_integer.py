#!/usr/bin/python3
"""A function that prints an integer"""


def safe_print_integer(value):
    """Safely prints an integer

    Args:
        value (int): The integer value to print.
    Returns:
        bool: True if the integer was successfully printed, False otherwise.
    """

    try:
        formatted_number = "{:d}".format(value)
        print(formatted_number)
        result = True
    except (ValueError, TypeError):
        result = False
    return result
