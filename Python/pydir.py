#!/bin/env python3

from os import listdir
from os import chdir
from os import getcwd
from fnmatch import filter
from shutil import copy2


def csv():
    for i in csvFiles:
        print("CSV file name is: {}".format(i))


def py():
    for i in pyFiles:
        print("Python file name is: {}".format(i))

def cop():
    copy2( dirk + "/linuxtips", dirk + "/code/Linguistics/Python/")

if __name__ == "__main__":


    CSV = "*.csv"
    PY  = "*.py"

    dirk = input("directory we want to look at: ")

    csvFiles = filter(listdir(dirk), CSV)
    pyFiles  = filter (listdir(dirk), PY)

    csv()
    py()
    cop()
