#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                n += 1
        print()
        return n
    except (TypeError, ValueError):
        print(end="")
        return n
