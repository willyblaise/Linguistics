import sys
import os
import datetime
from functools import reduce


if __name__ == "__main__":
    gas = []
    n = int(input("Please enter the number of times you went to the Gas station: "))
    dt = datetime.datetime.now().strftime("%B %C%y")

    for i in range(n):
        g = float(input(f"Please enter number {i}: "))
        gas.append(g)

    print(f"The total spent on gas for {dt} is: {reduce(lambda x,y : x + y, gas)}")
