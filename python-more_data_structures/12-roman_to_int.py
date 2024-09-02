#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dict = {"I": 1,
                  "V": 5,
                  "X": 10,
                  "L": 50,
                  "C": 100,
                  "D": 500,
                  "M": 1000}
    max_value = 0
    for index, number in enumerate(roman_string):
        if roman_dict[number] > max_value:
            max_value = roman_dict[number]
            idx = index

    sum = 0
    length = len(roman_string)
    if idx != 0:
        i = 0
        while i < idx:
            sum -= roman_dict[roman_string[i]]
            i = i + 1
    while idx < length:
        num = roman_dict[roman_string[idx]]
        if idx != length - 1:
            next_num = roman_dict[roman_string[idx + 1]]
            if idx != length - 1 and num < next_num:
                sum += next_num - num
                idx += 2
                continue
        sum += roman_dict[roman_string[idx]]
        idx += 1
    return sum
