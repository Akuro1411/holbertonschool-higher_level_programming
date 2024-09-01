#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = my_list[:]
    if idx < 0 or len(copy_list) <= idx:
        return copy_list
    copy_list[idx] = element
    return copy_list
