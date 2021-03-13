#!/bin/env python3


def sales_tax() -> int:
    x = int(input("Please give me the amount. "))
    tax = x * .0825
    total = tax + x
    return print("The Total after Tax is:" , total)

sales_tax()
