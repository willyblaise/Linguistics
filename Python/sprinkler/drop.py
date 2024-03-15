import sqlite3

# Connect to the database
conn = sqlite3.connect('sprinkler_system.db')
cursor = conn.cursor()

# Drop existing 'zones' table (if it exists) to avoid conflicts with the modified table
cursor.execute('DROP TABLE IF EXISTS zones')

# Create a new 'zones' table with schedule and run time columns
cursor.execute('''CREATE TABLE IF NOT EXISTS zones (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    description TEXT,
                    schedule TEXT,
                    run_time INTEGER
                )''')

# Insert sample data for zones (including schedule and run time)
zones_data = [
    (1, 'Zone 1', 'Front lawn', 'Monday,Wednesday,Friday 08:00', 30),
    (2, 'Zone 2', 'Back lawn', 'Tuesday,Thursday,Saturday 07:00', 20),
    (3, 'Zone 3', 'Flower bed', 'Monday,Wednesday 09:00', 15),
    (4, 'Zone 4', 'Vegetable garden', 'Tuesday,Thursday 10:00', 25),
    (5, 'Zone 5', 'Shrubs', 'Friday,Saturday 09:30', 20),
    (6, 'Zone 6', 'Trees', 'Monday,Wednesday,Saturday 10:30', 35),
    (7, 'Zone 7', 'Side yard', 'Tuesday,Thursday,Saturday 11:00', 30),
    (8, 'Zone 8', 'Fruit trees', 'Monday,Wednesday,Friday 11:30', 25)
]
cursor.executemany('INSERT INTO zones VALUES (?, ?, ?, ?, ?)', zones_data)

# Commit changes
conn.commit()

# Close connection
conn.close()

