#!/bin/env python3

import sys


def subtract(x, y) -> int:
    return x - y

def s(x=100, y=2) -> int:

    print(f"Your result after subtraction is: {subtract(x, y)}")


if __name__ == "__main__":

    if len(sys.argv) > 1:
        if int(sys.argv[1]) >= 0 and int(sys.argv[2]) >= 0:
            x = int(sys.argv[1])
            y = int(sys.argv[2])
            s(x,y)

    if len(sys.argv) < 2:
        s()
