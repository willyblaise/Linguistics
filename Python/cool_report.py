import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Step 1: Retrieve data from SQLite database
# (Assuming you have a SQLite database connection and a cursor)
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('path to your db')
cursor = conn.cursor()

# Execute your SQL query to retrieve data
cursor.execute('SELECT * FROM your_table ORDER BY created_at DESC LIMIT 5')
data = cursor.fetchall()

# Close the database connection when done
conn.close()

# 'data' now contains the results of your query
# Step 2: Format data (replace this with your formatting logic)


formatted_data = "<table style='border-collapse: collapse; width: 100%;'><tr><th>ID</th><th>Units</th><th>Meal</th><th>Date</th></tr>"

for row in data:
    formatted_data += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>"

formatted_data += "</table>"

# Step 3: Compose email
sender_email = "your@mail.com"
receiver_email = "receiver@mail"
subject = "Your Report"

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject



# Step 4: Attach data

body = f"""\
<html>
    <body>
        <p>Please find the report attached:</p>
        {formatted_data}
    </body>
</html>
"""

message.attach(MIMEText(body, 'html'))

# Step 5: Send email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender_email, 'your password')
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
