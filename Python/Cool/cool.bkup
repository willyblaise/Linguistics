#!/bin/env python3
from Medication import Medication
import sqlite3
import sys


conn = sqlite3.connect("/home/champ/sqlite/cool.db")
c = conn.cursor()

def close_db():
    c.close()
    conn.close()

def injections():
    while True:
        try:
            injections = int(input("How many injections do you want to input? "))
        except ValueError:
            print("Sorry, I don't understand that.")
            continue
        else:
            break

    if injections < 1:
        sys.exit("no injections to input")
    else:
        return injections

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS "inject" (id integer primary key autoincrement, Units integer, Meal BOOLEAN, "created_at" DATETIME DEFAULT CURRENT_TIMESTAMP, "subjectId" integer, CONSTRAINT fk_name FOREIGN KEY (subjectId) REFERENCES subject(id))')

def data_entry():

# The simplest way to accomplish this is to put the input method in a while loop. Use continue when you get bad input, and break out of the loop when you're satisfied.

# When Your Input Might Raise an Exception
# Use try and except to detect when the user enters data that can't be parsed.

    cool = Medication()

    while True:
        try:
            # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
            #patient = int(input("Please enter your Patient: "))
            cool.patient_id = int(input("Please enter your Patient: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            #better try again... Return to the start of the loop
            continue
        else:
            print("Patient number was successfully parsed!")
            print("we're ready to exit the loop.")
            break

    while True:
        try:
            # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
            #units = int(input("Please provide units: "))
            cool.units = int(input("Please provide units: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            #better try again... Return to the start of the loop
            continue
        else:
            #age was successfully parsed!
            #we're ready to exit the loop.
            break


    cool.meal = input("What did Cool eat? ")

    c.execute("INSERT INTO inject (Units, Meal, subjectId) values(?,?,?)", (cool.units, cool.meal, cool.patient_id))

    conn.commit()

def select_table():
    c.execute("SELECT * FROM inject")
    all_results = c.fetchall()
    for row in all_results:
        print(row)


if __name__ == "__main__":


    injections = injections()
    create_table()

    for i in range(injections):
        data_entry()

    select_table()
    close_db()
