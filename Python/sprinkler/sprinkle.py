import sqlite3

# Connect to the database (will create it if it doesn't exist)
conn = sqlite3.connect('sprinkler_system.db')
cursor = conn.cursor()

# Create a table for the schedule
cursor.execute('''CREATE TABLE IF NOT EXISTS schedule (
                    id INTEGER PRIMARY KEY,
                    day_of_week TEXT,
                    start_time TEXT,
                    duration INTEGER
                )''')

# Create a table for the zones
cursor.execute('''CREATE TABLE IF NOT EXISTS zones (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    description TEXT
                )''')

# Insert sample data for zones
zones_data = [
    (1, 'Zone 1', 'Front lawn'),
    (2, 'Zone 2', 'Back lawn'),
    (3, 'Zone 3', 'Flower bed'),
    (4, 'Zone 4', 'Vegetable garden'),
    (5, 'Zone 5', 'Shrubs'),
    (6, 'Zone 6', 'Trees'),
    (7, 'Zone 7', 'Side yard'),
    (8, 'Zone 8', 'Fruit trees')
]
cursor.executemany('INSERT INTO zones VALUES (?, ?, ?)', zones_data)

# Commit changes
conn.commit()

# Close connection
conn.close()

