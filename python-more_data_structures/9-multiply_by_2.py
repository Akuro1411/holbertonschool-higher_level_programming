#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiplied_dict = {key: a_dictionary[key] * 2 for key in list(a_dictionary)}
    return multiplied_dict
