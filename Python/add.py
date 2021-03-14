#!/bin/python

import sys

name = sys.argv[0]


def summed_up():
    global sum
    for number in range(1, len(sys.argv)):
        sum += int(sys.argv[number])

    print(f"{sum} is the sum of all passed in Arguments")


if __name__ == "__main__":

    print(f"{name.upper()} is the name of this application.")
    sum = 0
    summed_up()
