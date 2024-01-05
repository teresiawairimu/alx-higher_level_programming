#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Remove the item at a specified position in the given list and return the modified list."""
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return my_list
