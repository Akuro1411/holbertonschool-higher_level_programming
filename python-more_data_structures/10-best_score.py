#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return 
    num = 0
    for i in a_dictionary:
        if num == 0 and a_dictionary[i] != 0:
            num = a_dictionary[i]
        if a_dictionary[i] > num:
            num = a_dictionary[i]
    return num
