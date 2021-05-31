#!/bin/env python3

import sys
from os import listdir
from os import chdir
from os import getcwd

filename = sys.argv[1]

def readfile():
    with open(filename, 'rb') as f:
        while True:
            line = f.readline()
            print(line)
            if not line:
                break


if __name__ == "__main__":
    readfile()
    print(f"Current Directory is: {getcwd()}")
    print("The following is the directory contents")
    ld = listdir()
    for n in ld:
        print(n)
