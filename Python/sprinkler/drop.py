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
    (1, 'Zone 1', 'Flower Bed', 'Monday,Wednesday,Friday 08:00', 10),
    (2, 'Zone 2', 'Front lawn', 'Tuesday,Thursday,Saturday 07:00', 10),
    (3, 'Zone 3', 'Right Side', 'Monday,Wednesday 09:00', 15),
    (4, 'Zone 4', 'Unknown', 'Tuesday,Thursday 10:00', 15),
    (5, 'Zone 5', 'Back - Left', 'Friday,Saturday 09:30', 10),
    (6, 'Zone 6', 'Left Side', 'Monday,Wednesday,Saturday 10:30', 15)
]
cursor.executemany('INSERT INTO zones VALUES (?, ?, ?, ?, ?)', zones_data)

# Commit changes
conn.commit()

# Close connection
conn.close()

