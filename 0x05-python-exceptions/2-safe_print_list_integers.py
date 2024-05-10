#!/usr/bin/python3
"""prints the first x elements of a list and only integers"""


def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers

       Args:
           my_list: The name of the list that can contain any type
           x: The number of elements from the list that are printed.
           Can be bigger than the length of my_list,
           if that's the case an exception is expected to occur
       Returns:
              The real number of integers printed
    """
    try:
        number_of_printed_integers = 0
        for i in range(x):
            if isinstance(my_list[i], int):
                formatted_element = "{:d}".format(my_list[i])
                print(formatted_element, end='')
                number_of_printed_integers += 1
        print()
        return number_of_printed_integers
    except IndexError:
        raise
