#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = list(a_dictionary.keys())
    new_dict.sort()
    sorted_dict = {i: a_dictionary[i] for i in new_dict}
    for i in sorted_dict:
        print(f"{i}: {sorted_dict[i]}")
