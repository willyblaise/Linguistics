#!/bin/python

import sys

sum = 0

for number in range(1, len(sys.argv)):
    sum += int(sys.argv[number])

print(sum)
