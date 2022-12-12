import sqlite3

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

    except sqlite3.OperationalError:
        print("No such table in db: cool.db")
        if(sqlite3.OperationalError):
            try:
                print("Creating a new table: ")
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

    except sqlite3.OperationalError:
        print("No such file or db: cool_pens")
        if(sqlite3.OperationalError):
            try:
                print("Creating a new table: ")
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

    if answer == 1:
        injects()
    elif answer == 2:
        pens()
    else:
        print("There is Nothing to do here.")



    connection.commit()
    connection.close()

