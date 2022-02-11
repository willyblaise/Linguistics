import sqlite3
import sys

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
    c.execute("SELECT * FROM inject")


if __name__ == "__main__":

    injections = int(input("How many injections do you want to input?"))

    if injections < 1:
        sys.exit("no injections to input")

    for i in range(injections):
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
