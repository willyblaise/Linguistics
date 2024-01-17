import sqlite3
import logging
import redis


#conn = sqlite3.connect("/home/jimmycooks/sqlite/cool.db")
#c = conn.cursor()

class DatabaseManager:
    def __init__(self, db_path='/home/jimmycooks/sqlite/cool_orig.db'):
        self.db_path = db_path
        self.connection = None
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.commit()
            self.connection.close()

    def _create_inject_table(self, cur):
        # Your existing table creation code here
        self.connection.execute('CREATE TABLE IF NOT EXISTS "inject" (id integer primary key autoincrement, Units integer, Meal BOOLEAN, "created_at" DATETIME DEFAULT CURRENT_TIMESTAMP, "subjectId" integer, CONSTRAINT fk_name FOREIGN KEY (subjectId) REFERENCES subject(id))')

    def _create_pens_table(self, cur):
        # Your existing table creation code here
        self.connection.execute('''CREATE TABLE IF NOT EXISTS "cool_pens" (
                id integer Primary Key AUTOINCREMENT,
                PLACE text,
                price float,
                date date
            )''')


    def fetch_and_cache_data(self, query, cache_key):
        cached_data = self.redis_client.get(cache_key)
        c = 0
        if cached_data:
            print(f"Reading from Redis cache for {cache_key}:")
            for row in eval(cached_data):
                print(row)
                c += 1
                if c == 15:
                    break
            logging.info(f"Successfully returned results from cache for {cache_key}.")
        else:
            try:
                cur = self.connection.cursor()
                cur.execute(query)
                data_list = cur.fetchall()
                print(f'Retrieved fresh data for {cache_key}:')
                for i in data_list:
                    print(i)

                # Store data in Redis cache
                self.redis_client.set(cache_key, str(data_list))
                logging.info(f"Successfully returned results and stored in cache for {cache_key}.")
            except sqlite3.OperationalError:
                logging.error(f"No such table in db: {self.db_path}")
                logging.info(f"Something bad happened on the {cache_key} select.")
                cur = self.connection.cursor()
                if "inject" in cache_key:
                    self._create_inject_table(cur)
                else:
                    self._create_pens_table(cur)

    def injects(self):
        query = "SELECT * FROM inject desc LIMIT 15"
        cache_key = 'injects_data'
        self.fetch_and_cache_data(query, cache_key)

    def pens(self):
        query = "SELECT * FROM cool_pens"
        cache_key = 'pens_data'
        self.fetch_and_cache_data(query, cache_key)

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

