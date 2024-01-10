#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    x = sorted(a_dictionary.keys())
    for item in x:
        print(f"{item}: {a_dictionary[item]}")
