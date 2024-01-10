#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    keys = list(a_dictionary.keys())
    for item in keys:
        #if isinstance(item, str):
            if item == key:
                a_dictionary[item] = value
            else:
                a_dictionary[key] = value
    return a_dictionary
