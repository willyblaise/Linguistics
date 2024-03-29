import sqlite3
from contextlib import contextmanager
import random

# Context manager to handle SQLite connections and transactions
@contextmanager
def sqlite_cursor():
    conn = sqlite3.connect("bank_accounts.db")
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = None  # Will be assigned when persisted

    def generate_unique_account_number(self):
        while True:
            account_number = random.randint(100000, 999999)
            if not self.is_account_number_exists(account_number):
                return account_number

    def is_account_number_exists(self, account_number):
        with sqlite_cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM bank_accounts WHERE account_number = ?", (account_number,))
            return cursor.fetchone()[0] > 0

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit of ${amount} successful. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal of ${amount} successful. New balance: ${self.balance}"
        else:
            return "Insufficient funds. Withdrawal failed."

    def persist(self):
        self.account_number = self.generate_unique_account_number()
        with sqlite_cursor() as cursor:
            cursor.execute("INSERT INTO bank_accounts (account_number, account_holder, balance) VALUES (?, ?, ?)",
                           (self.account_number, self.account_holder, self.balance))


    def check_balance(self):
        if self.account_number is not None:
            with sqlite_cursor() as cursor:
                cursor.execute("SELECT balance FROM bank_accounts WHERE account_number = ?", (self.account_number,))
                result = cursor.fetchone()
                if result:
                    self.balance = result[0]
                    return f"Current balance: ${self.balance}"
        return "Account not found or balance not available."

    @classmethod
    def load_from_db(cls, account_number):
        with sqlite_cursor() as cursor:
            cursor.execute("SELECT account_holder, balance FROM bank_accounts WHERE account_number = ?", (account_number,))
            result = cursor.fetchone()
            if result:
                account_holder, balance = result
                return cls(account_holder, balance)
            else:
                return None

# Create the SQLite table
with sqlite_cursor() as cursor:
    cursor.execute("CREATE TABLE IF NOT EXISTS bank_accounts (id INTEGER PRIMARY KEY, account_number INTEGER, account_holder TEXT, balance REAL)")

# Example usage:
#account = BankAccount("Charlie Brown", 2000)
#account.deposit(800)
#account.persist()
#print(f"Account number: {account.account_number}")

existing_account_number = 940378 # Replace with an actual account number from the database
print(f"Existing Account Number:{existing_account_number}")
existing_account = BankAccount.load_from_db(existing_account_number)

if existing_account:
    print(existing_account.check_balance())
else:
    print("Account not found.")
