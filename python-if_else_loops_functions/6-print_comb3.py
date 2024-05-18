#!/usr/bin/python3
for i in range(1, 100, 11):
    if (i == 89):
        break
    while (i % 10 != 0):
        print(f"{'{:02d}'.format(i)}, ", end="")
        i = i+1
print("89")
