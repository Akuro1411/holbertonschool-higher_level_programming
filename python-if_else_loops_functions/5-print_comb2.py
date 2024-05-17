#!/usr/bin/python3
for i in range(100):
    if i == 99:
        break
    print(f"{'{:02d}'.format(i)}, ", end="")
print("99")
