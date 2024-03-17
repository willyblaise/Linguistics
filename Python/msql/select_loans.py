

import mysql.connector

# Replace these with your own database credentials
host = 'localhost'
user = 'champ'
password = 'loga'
database = 'family_loans'

# Establish a connection to the MySQL server
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Example SQL query to fetch records from a table (replace 'your_table' with your actual table name)
query = "SELECT * FROM loans"

# Execute the query
cursor.execute(query)

# Fetch all records
records = cursor.fetchall()

# Display headers
headers = ["Loan_id", "Borrower Name", "Loan Amount", "Interest Rate", "Start Date", "Payoff Date", "Status", "Created At", "Updated At"]
print("\t".join(headers))

# Display the records
for record in records:
    print(record)
    
    
# Close the cursor and connection
cursor.close()
connection.close()
