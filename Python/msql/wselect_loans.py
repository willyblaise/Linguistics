import mysql.connector

# Database connection details
host = "localhost"
user = "champ"
password = "loga"
database = "family_loans"

# Establishing connection using 'with' context manager
with mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
) as connection:
    # Create a cursor object to execute SQL queries
    with connection.cursor() as cursor:
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
