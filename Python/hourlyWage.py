#!/bin/python


def hourly_wage():
    try:
        salary = int(input("What is your yearly salary? "))

    except ValueError:
        print("PLEASE ENTER A NUMBER TO CALCULATE YOUR SALARY unless your Salary is in ROMAN NUMERALS.")

    hourly_wage = salary / 2080
    return print("Your Hourly Wage is {}".format(hourly_wage))


hourly_wage()
