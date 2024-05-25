#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    length_a = len(a)
    length_b = len(b)

    if length_a > length_b:
        t = length_a - length_b
        for i in range(t):
            b.append(0)
    elif length_b > length_a:
        t = length_b - length_a
        for i in range(t):
            a.append(0)

    new_list = []
    for j in range(len(a)):
        new_list.append(a[j] + b[j])
    new_tup = tuple(new_list)
    return new_tup
