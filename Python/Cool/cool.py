#!/bin/env python3
from Medication import Medication
from Pens import Pens
from cool_select import *
from pathlib import Path
import sqlite3
import sys
import logging

logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="cool.log"
        )


conn = sqlite3.connect("///sqlite/cool.db")
c = conn.cursor()

def close_db():
    c.close()
    conn.close()

def injections():
    while True:
        try:
            injections: int = int(input("How many injections do you want to input? "))
        except ValueError:
            logging.error("Something other than a Number was entered.")
            print("Sorry, I don't understand that.")
            continue
        else:
            break

    if injections < 1:
        sys.exit("no injections to input")
    else:
        logging.info(f"{injections} injection this time.")
        return injections

def create_table() -> None:
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
            logging.info("Entering patient ID information.")
            cool.patient_id = int(input("Please enter your Patient: "))
        except ValueError:
            logging.error("Something other than a Number was entered for Patient.")
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

    while True:
        try:
            cool.f_units: float = float(input("Please provide units in Float: "))
        except ValueError:
            print("Sorry, I didn't understand that, doesn't seem like a Float.")
            #better try again... Return to the start of the loop
            continue
        else:
            print("float was successfully parsed!")
            #we're ready to exit the loop.
            break

    cool.meal: str = input("What did Cool eat? ")

    c.execute("INSERT INTO inject (Units, Float_Units, Meal, subjectId) values(?,?,?,?)", (cool.units, cool.f_units, cool.meal, cool.patient_id))

    conn.commit()
    logging.info("Shot Records successfully entered.")


def pen_insert():

    pen_info: float = Pens()
    
    pen_info.pharmacy: str = input("What pharmacy was this purchased? ")
    pen_info.price: float = float(input("What is the price? "))

    try:
        c.execute("INSERT INTO cool_pens (Place, Price) values(?,?)", (pen_info.pharmacy, pen_info.price))
    except:
        logging.error("DB information was not Entered")


    conn.commit()
    logging.info("Cool's new Pen successfully entered.")



def select_table():
    try:
        lim: int = int(input("Please enter the limit: "))
        rsql: dict = Path("/home/jimmycooks/apps/sql/sinject.sql").read_text()
        placeholder: dict = { "limit": lim }
        logging.info("Select is about to Transpire on the DB.")
        c.execute(rsql, placeholder)
        all_results: list = c.fetchall()
    except sqlite3.Error as er:
        logging.error("Something bad happened during the db selection.")

    for row in all_results:
        print(row)


if __name__ == "__main__":

    try:
        ans: str = input("Do you want to check Cool's pen information? y or n: ")
        logging.info("This query is NOT for a pen")
    except ValueError:
        logging.error("Improper value put in for Pen.")

    if ans == "y":
        pen: bool = True
    else:
        pen: bool = False

    if pen:
        pens()

    try:
        answer: str = input("Do you want to add a New pen? y or n: ")
        logging.info("This query IS for a pen")
    except ValueError:
        logging.error("Improper value put in for Pen.")


    if answer == "y":
        new_pen: bool = True
    else:
        new_pen: bool = False

    if new_pen:
        pen_insert()
        sys.exit()

    injections: int = injections()
    create_table()

    for i in range(injections):
        data_entry()

    select_table()
    close_db()
