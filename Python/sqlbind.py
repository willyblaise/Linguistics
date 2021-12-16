import sqlite3
import sys

conn = sqlite3.connect("computers.db")

c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS people (id integer primary key autoincrement, Number REAL, Name Text)')



def data_entry():
    number = input("Please provide a house number: ")
    name = input("Please provide a name: ")

    c.execute("INSERT INTO people (Number, Name) values(?,?)", (number, name))

    conn.commit()

def select_table():
    c.execute("SELECT * FROM people")


if __name__ == "__main__":

    people = int(input("How many people do you want to input?"))

    if people < 1:
        sys.exit("no people to input")

    for i in range(people):
        create_table()
        data_entry()


    select_table()
    results = c.fetchone()
    all_results = c.fetchall()
#    print(f"{all_results}")

    for row in all_results:
        print(row)


    c.close()
    conn.close()
