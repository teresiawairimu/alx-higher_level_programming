#!/usr/bin/python3
def no_c(my_string):
    """define a function that eliminates all occurrences of the characters 'c' and 'C' from a provided string."""
    new_string = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_string += my_string[i]
    return new_string
