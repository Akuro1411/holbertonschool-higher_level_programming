#!/usr/bin/python3
def no_c(my_string):
    new_list = list(my_string)
    for i in range(len(new_list)):
        if new_list[i] == 'c' or new_list[i] == 'C':
            new_list[i] = ""
    new_string = ''.join(new_list)
    return new_string
