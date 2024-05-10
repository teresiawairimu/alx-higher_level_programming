#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints the specified number of elements on a list

    Args:
        my_list(list): A list containing the elements.
        x(int): the integer that specifies the number of elements to print

    Returns:
        The number of elements that are printed
    """
    number = 0
    for element in range(x):
        try:
            print(my_list[element], end='')
            number += 1
        except IndexError:
            break
    print()
    return number
