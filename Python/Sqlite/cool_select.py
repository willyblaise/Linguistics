import sqlite3
import sys
from pathlib import Path

conn = sqlite3.connect("cool.db")

c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS "inject" (id integer primary key autoincrement, Units integer, Meal BOOLEAN, "created_at" DATETIME DEFAULT CURRENT_TIMESTAMP, "subjectId" integer, CONSTRAINT fk_name FOREIGN KEY (subjectId) REFERENCES subject(id))')

def data_entry():
    patient  = input("Please provide a ID: ")
    units    = input("Please provide units: ")
    meal     = input("Did Cool eat? ")

    c.execute("INSERT INTO inject (Units, Meal, subjectId) values(?,?,?)", (units, meal, patient))

    conn.commit()

def select_table():
#    c.execute("SELECT * FROM inject")
    lim = 10
    lim = int(input("What is the limit you would like: "))
    rsql = Path("sql/inject.sql").read_text()
    placeholder = { "limit": lim }
    c.execute(rsql, placeholder)


if __name__ == "__main__":

    select_table()
    results = c.fetchone()
    all_results = c.fetchall()
#   print(f"{all_results}")

    for row in all_results:
        print(row)

    c.close()
    conn.close()
