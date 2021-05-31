#!/bin/env python3



def prime(num) -> bool:
    isPrime = True

    for i in range(2, num):
        if num % i == 0:
            isPrime = False

    return isPrime


max_num = int(input("Please enter Max Prime Number to check."))

for i in range(2, max_num):
    if prime(i):
        print(f"{i} is a Prime Number.")
