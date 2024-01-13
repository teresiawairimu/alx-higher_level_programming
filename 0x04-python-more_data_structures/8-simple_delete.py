#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    key_copy = a_dictionary.keys()
    for key in key_copy:
        if isinstance(key, str):
            del(key)
    return a_dictionary

