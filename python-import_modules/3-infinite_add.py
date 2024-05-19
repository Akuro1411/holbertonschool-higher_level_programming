#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    sum_of_elements = 0
    i = 1
    while i < len(argv):
        sum_of_elements += int(argv[i])
        i += 1
    print(f"{sum_of_elements}")
