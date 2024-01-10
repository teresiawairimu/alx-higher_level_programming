#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    new_set = set()
    for item in my_list:
        if item not in new_set:
            result += item
            new_set.add(item)
    return result
