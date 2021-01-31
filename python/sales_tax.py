#!/bin/python


def sales_tax():
    x = int(input("Please give me the amount. "))
    tax = x * .0825
    total = tax + x
    return print("the total is:" , total)

sales_tax()
