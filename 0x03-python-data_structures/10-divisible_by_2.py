#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Identify all elements in a list that are multiples of 2 and return a corresponding boolean list."""
    multiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return multiples
