#!/bin/env python3

from os import listdir
from fnmatch import filter



def csv():
    for i in csvFiles:
        print("CSV file name is: {}".format(i))


def py():
    for i in pyFiles:
        print("Python file name is: {}".format(i))


if __name__ == "__main__":


    CSV = "*.csv"
    PY  = "*.py"

    csvFiles = filter(listdir("./Data"), CSV)
    pyFiles  = filter (listdir("."), PY)

    csv()
    py()
