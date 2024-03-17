import sqlite3

def select_all_zones():
    """
    select all zones from the db
    """
    conn = sqlite3.connect('sprinkler_system.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM zones')
    zones = cursor.fetchall()

    conn.close()

    return zones

def select_zone_by_id(zone_id):
    """
    select zone by id
    """
    conn = sqlite3.connect('sprinkler_system.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM zones WHERE id = ?', (zone_id,))
    zone = cursor.fetchone()

    conn.close()

    return zone

if __name__ == "__main__":
    all_zones = select_all_zones()
    print("All Zones:")
    for zone in all_zones:
        print(zone)

    print("\nZone Details:")
    zone_id = int(input("Zone ID you want to check: "))
    zone = select_zone_by_id(zone_id)
    if zone:
        print(zone)
    else:
        print(f"Zone with ID {zone_id} not found.")
