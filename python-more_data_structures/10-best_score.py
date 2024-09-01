#!/usr/bin/python3
def best_score(a_dictionary):
    max_key = ""
    max_value = 0
    if a_dictionary is not None and a_dictionary != {}:
        for key, item in a_dictionary.items():
            if item > max_value:
                max_value = item
                max_key = key
        return max_key
    return None
