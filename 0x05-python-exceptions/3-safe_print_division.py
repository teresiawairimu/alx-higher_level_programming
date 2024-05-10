#!/usr/bin/python3
"""Divides 2 integers and prints the result"""


def safe_print_division(a, b):
    """Divides 2 integers and prints the result

       Args:
           a(int): The first integer
           b(int): The second integer
        Returns:
           The value of the division, otherwise None

    """

    try:
        result = a / b
    except ZeroDivisionError:
        pass
    except Exception as e:
        pass
    finally:
        if 'result' in locals():
            print("Inside result: {}".format(result))
            return result
        else:
            result = None
            print("Inside result: {}".format(result))
            return result
