import sqlite3
import logging


logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H%M%S",
        filename="cool_select.log"
        )


connection = sqlite3.connect('/home/jimmycooks/sqlite/cool.db')
cur = connection.cursor()

def injects():

    try:
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
        if(sqlite3.OperationalError):
            try:
                logging.info("Creating a new table: ")
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

            except sqlite3.Error() as e:
                print(e, " occurred")


def pens():

    try:
        cur.execute("SELECT * FROM cool_pens")
        data_list = cur.fetchall()
        print('ID' + 'Pharmacy' + '\t Price' + '      Date')
        print('------------' + '--------------' + '--------')

        logging.info("Successfully returned Pen information.")

    except sqlite3.OperationalError:
        logging.error("No such file or db: cool_pens")
        if(sqlite3.OperationalError):
            try:
                logging.info("Creating a new table: ")
                cur.execute('''
                CREATE TABLE cool_pens(
                    id integer Primary Key AUTOINCREMENT,
                    PLACE text,
                    price float,
                    date date
                )''')
                print("New table created successfully!")
                print("Here are the contents of the table: \n1: id \n2: place \n3: price \n4: date.")

            except sqlite3.Error() as e:
                print(e, " occurred")



if __name__ == "__main__":
    answer = int(input("Press 1 for Injects or 2 for Pens: "))
    logging.info(f"You are checking for {answer}")

    if answer == 1:
        injects()
    elif answer == 2:
        pens()
    else:
        print("There is Nothing to do here.")
        logging.info("Looks like you chose something that is not done by this app.")



    connection.commit()
    connection.close()
