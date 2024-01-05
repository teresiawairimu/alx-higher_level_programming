#!/usr/bin/python3
def max_integer(my_list=[]):
    """Returns the maximum integer in a given list. Returns None if the list is empty."""
    if len(my_list) == 0:
        return (None)

    big = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > big:
            big = my_list[i]
