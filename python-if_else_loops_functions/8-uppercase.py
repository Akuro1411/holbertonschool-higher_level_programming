#!/usr/bin/python3
def uppercase(str):
    for i in str:
        number = ord(i)
        if number >= 97 and number <= 122:
            number = number - 32
            print(chr(number).format(i), end="")
        else:
            print(i, end="")
