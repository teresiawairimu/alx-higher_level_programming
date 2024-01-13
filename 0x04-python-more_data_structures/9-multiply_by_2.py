#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict()
    for item in a_dictionary.keys():
        a = a_dictionary[item]
        b = a*2
        new_dict[item] = b
    return new_dict
