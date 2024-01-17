import logging
from pathlib import Path
import sqlite3
from dataclasses import dataclass
import os

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="cool.log"
)

@dataclass
class Medication:
    patient_id: int
    units: int
    f_units: float
    meal: str

@dataclass
class Pens:
    pharmacy: str
    price: float

class CoolDatabaseManager:
    def __init__(self, db_path=os.environ.get("COOL_DB")):
        self.db_path = db_path
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.commit()
            self.connection.close()

    def close_db(self):
        if self.connection:
            self.connection.close()

    def create_table(self):
        try:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS "inject" (id INTEGER PRIMARY KEY AUTOINCREMENT, Units INTEGER, Meal BOOLEAN, "created_at" DATETIME DEFAULT CURRENT_TIMESTAMP, "subjectId" INTEGER, CONSTRAINT fk_subject FOREIGN KEY ("subjectId") REFERENCES subject(id))')
            logging.info("Table 'inject' created successfully.")
        except sqlite3.Error as er:
            logging.error(f"Error creating table 'inject': {er}")

    def data_entry(self):
        cool = Medication(patient_id=100, units=3, f_units=3.0, meal="Hibachi")

        while True:
            try:
                logging.info("Entering patient ID information.")
                cool.patient_id = int(input("Please enter your Patient: "))
            except ValueError:
                logging.error("Invalid input for Patient. Please enter a number.")
                print("Sorry, I didn't understand that.")
                continue
            else:
                print("Patient number was successfully parsed!")
                print("Ready to exit the loop.")
                break

        while True:
            try:
                cool.units = int(input("Please provide units: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:
                break

        while True:
            try:
                cool.f_units = float(input("Please provide units in Float: "))
            except ValueError:
                print("Sorry, I didn't understand that, doesn't seem like a Float.")
                continue
            else:
                print("Float was successfully parsed!")
                break

        cool.meal = input("What did Cool eat? ")

        try:
            self.cursor.execute("INSERT INTO inject (Units, Float_Units, Meal, subjectId) values(?,?,?,?)", (cool.units, cool.f_units, cool.meal, cool.patient_id))
            logging.info("Shot Records successfully entered.")
        except sqlite3.Error as er:
            logging.error(f"Error entering shot records: {er}")

    def pen_insert(self):
        pen_info = Pens(pharmacy="Walgreens", price=103.50)
        pen_info.pharmacy = input("What pharmacy was this purchased? ")

        while True:
            try:
                pen_info.price = float(input("What is the price? "))
                break
            except ValueError:
                print("Sorry, I didn't understand that. Please enter a valid number.")

        try:
            self.cursor.execute("INSERT INTO cool_pens (Place, Price) values(?,?)", (pen_info.pharmacy, pen_info.price))
            logging.info("Cool's new Pen successfully entered.")
        except sqlite3.Error as er:
            logging.error(f"Error entering pen information: {er}")

    def check_pen_info(self):
        try:
            logging.info("Checking Cool's pen information.")
            self.cursor.execute("SELECT * FROM cool_pens")
            all_results = self.cursor.fetchall()
        except sqlite3.Error as er:
            logging.error(f"Error checking pen information from the database: {er}")

        for row in all_results:
            print(row)

    def select_table(self):
        all_results = None
        try:
            lim = int(input("Please enter the limit of records you'd like returned: "))
            rsql = Path("/home/jimmycooks/apps/sql/sinject.sql").read_text()
            placeholder = {"limit": lim}
            logging.info("Select is about to transpire on the DB.")
            self.cursor.execute(rsql, placeholder)
            all_results = self.cursor.fetchall()
        except sqlite3.Error as er:
            logging.error(f"Error selecting from the database: {er}")

        if all_results is not None:
            for row in all_results:
                print(row)
        else:
            print("Nothing to Parse here.")

    def main(self):
        try:
            answer = input("Do you want to add a new pen? y or n: ").lower()
            logging.info("Deciding to add a new pen or not.")
        except ValueError:
            logging.error("Improper value put in for Pen.")

        if answer == "y":
            self.pen_insert()

        try:
            need_injections = input("Do you need to add injections? y or n: ").lower()
        except ValueError:
            logging.error("Invalid input for the need of injections.")

        # Create the table only if injections are needed
        if need_injections == "y":
            self.create_table()

            try:
                injections = int(input("Enter the number of injections: "))
            except ValueError:
                logging.error("Invalid input for the number of injections. Please enter a valid number.")

            for _ in range(injections):
                self.data_entry()

        # Now, call the select_table method as the last line
        self.select_table()
        #print("No injections, Bye for now!")

if __name__ == "__main__":
    with CoolDatabaseManager() as db_manager:
        db_manager.main()
