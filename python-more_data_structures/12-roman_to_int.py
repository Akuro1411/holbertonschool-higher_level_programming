#!/usr/bin/python3
def roman_to_int(roman_string):
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
    if idx != 0:
        i = 0
        while i < idx:
            sum -= roman_dict[roman_string[i]]
            i = i + 1
    while idx < len(roman_number):
        sum += roman_dict[roman_string[idx]]
        idx += 1
    return sum
