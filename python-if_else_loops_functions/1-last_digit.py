#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = "Last digit of "
num = f"{number} is "
last_digit = number % 10
if last_digit > 5:
    string_sec = "and is greater than 5"
elif last_digit == 0:
    string_sec = "and is 0"
elif last_digit < 6 and last_digit != 0:
    string_sec = "and is less than 6 and not 0"
print(string + num + f"{last_digit} " + string_sec )
