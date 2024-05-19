#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print(f"{a} + {b} = {'{:n}'.format(add(a, b))}")
    print(f"{a} - {b} = {'{:n}'.format(sub(a, b))}")
    print(f"{a} * {b} = {'{:n}'.format(mul(a, b))}")
    print(f"{a} / {b} = {'{:n}'.format(div(a, b))}")
