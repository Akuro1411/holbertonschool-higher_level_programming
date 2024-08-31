#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if i % 2 == 1:
        print(chr(i - 32), end="")
        continue
    print(chr(i), end="")

# You can get reverse successive object with this way
# for i in range(122, 96, -1):
#     print(chr(i), end=" ")
