#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or len(my_list) == 0:
        return my_list
    cpy_list = []
    for index, i in enumerate(my_list):
        if index != idx:
            cpy_list.append(i)
    return cpy_list
