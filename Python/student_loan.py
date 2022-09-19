import os
from dataclasses import dataclass


@dataclass
class People:
    name: str
    age: int
    occupation: str






def daily_interest(irate: float, principal: float) -> float:
    irate = irate / 100
    annual = irate / 365
    annual_interest = (principal * annual) * 365
    return annual_interest




if __name__ == "__main__":
    rate = float(input("Please enter an Interest Rate: "))
    loan_amount = float(input("Please enter the loan amount: "))
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    job = input("What is your job? ")

    person = People(name, age, job)
    person2 = person



    print(f"{person.name} your annual interest rate for a {daily_interest(rate, loan_amount)}")
    print(f"{person2.name} hopefully you will have that {loan_amount} paid off soon as possible or better yet forgiven by Jim Crow Joe.")
