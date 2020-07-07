#!/bin/python


def add2(f,s):
    try:
        f = int(input("can i get the first number? "))
        s = int(input("can i get the second number? "))
        sum = f + s
        print(sum)

    except ValueError:
        print("%s or %s is not right, please tell Nicoles Ass" % (f, s))

add2('a','b')
