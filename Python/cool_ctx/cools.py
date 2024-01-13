import os
import sqlite3
import logging

class DatabaseManager:
    def __init__(self, db_path=os.environ.get("COOL_DB")):
        self.db_path = db_path
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        print("Entering Context.....")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            print("Exiting...")
            self.connection.commit()
            self.connection.close()

    def _create_inject_table(self, cur):
        try:
            cur.execute('''
            CREATE TABLE IF NOT EXISTS inject(
                id integer primary key autoincrement,
                Units integer,
                Meal BOOLEAN,
                "created_at" DATETIME DEFAULT CURRENT_TIMESTAMP,
                "subjectId" integer,
                CONSTRAINT fk_name FOREIGN KEY (subjectId) REFERENCES subject(id)
            )''')
            print("New table created successfully!")
            print("Here are the contents of the table: \n1: id \n2: place \n3: price \n4: date.")
        except sqlite3.Error as e:
            print(e, " occurred")

    def _create_pens_table(self, cur):
        try:
            cur.execute('''
            CREATE TABLE IF NOT EXISTS cool_pens(
                id integer Primary Key AUTOINCREMENT,
                PLACE text,
                price float,
                date date
            )''')
            print("New table created successfully!")
            print("Here are the contents of the table: \n1: id \n2: place \n3: price \n4: date.")
        except sqlite3.Error as e:
            print(e, " occurred")

    def injects(self):
        try:
            cur = self.connection.cursor()
            cur.execute("SELECT * FROM inject")
            data_list = cur.fetchall()
            print('ID' + 'Units' + '\t Meal' + '      Date')
            print('------------' + '--------------' + '--------')
            for i in data_list:
                print(i)
            logging.info("Successfully returned inject results.")
        except sqlite3.OperationalError:
            logging.error("No such table in db: cool.db")
            logging.info("Something bad happened on the inject select.")
            cur = self.connection.cursor()
            self._create_inject_table(cur)

    def pens(self):
        try:
            cur = self.connection.cursor()
            cur.execute("SELECT * FROM cool_pens")
            data_list = cur.fetchall()
            print('ID' + 'Pharmacy' + '\t Price' + '      Date')
            print('------------' + '--------------' + '--------')
            for i in data_list:
                print(i)
            logging.info("Successfully returned Pen information.")
        except sqlite3.OperationalError:
            logging.error("No such file or db: cool_pens")
            cur = self.connection.cursor()
            self._create_pens_table(cur)

if __name__ == "__main__":
    answer = int(input("Press 1 for Injects or 2 for Pens: "))
    logging.info(f"You are checking for {answer}")

    with DatabaseManager() as db_manager:
        if answer == 1:
            db_manager.injects()
        elif answer == 2:
            db_manager.pens()
        else:
            print("There is Nothing to do here.")
            logging.info("Looks like you chose something that is not done by this app.")
