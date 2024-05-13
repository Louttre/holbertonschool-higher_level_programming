#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return 0
    unique_elements = set()
    for i in my_list:
        unique_elements.add(i)
    return sum(unique_elements)
