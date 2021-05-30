#!/bin/env python3

import sys

def sales_tax() -> int:
    x = int(input("Please provide the subtotal: "))
    tax = x * 1.0825
    #total = tax + x
    return print("The Total after Tax is: " , tax)


def pchg():
    cv = int(input("Please provide the current value: "))
    iv = int(input("Please provide the initial value: "))
    pc = (cv - iv)/iv * 100
    return print("The percentage change is {}".format(pc))






if __name__ == "__main__":

    print(
            '''
            Please Choose one of the following options:

            1) Calculate Sales Tax

            2) Calculate Percentage Change

            3) Exit
            '''
        )

    option = int(input("Option: "))

    if   option == 1:
        sales_tax()
    elif option == 2:
        pchg()
    elif option == 3:
        sys.exit("Thanks for coming by!")
    else:
        print("Improper option chosen.")

