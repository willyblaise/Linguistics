#!/bin/python


def hourly_wage():
	salary = int(input("What is your yearly salary? "))
	hourly_wage = salary / 2080
	return print("Your Hourly Wage is {}".format(hourly_wage))


hourly_wage()
