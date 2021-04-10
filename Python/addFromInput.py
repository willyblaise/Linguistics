#!/bin/python


def add2():
    try:
        f = int(input("can i get the first number? "))
        s = int(input("can i get the second number? "))
        sum = f + s
        print(sum)

    except ValueError:
        print("Please tell Nicole's Ass the Wrong Data was Entered.")
        print("We need Integers for this to work.")


if __name__ == "__main__":

    add2()
