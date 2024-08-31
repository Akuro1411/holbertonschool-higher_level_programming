#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if i % 2 == 1:
        i = i - 32
    print(chr(i), end="")

# You can get reverse successive object with this way
# for i in range(122, 96, -1):
#     if i % 2 == 1:
#         i = i - 32
#     print(chr(i), end="")
