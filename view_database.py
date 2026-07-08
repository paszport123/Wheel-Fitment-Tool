import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

print("\n=== DATABASE VIEWER ===")
print("1 - Rims")
print("2 - Tires")
print("3 - Tire-Rim Measurements")
print("4 - Motorcycles")
print("5 - Show tables")
print("6 - Show table structure")

choice = input("\nChoose option: ")

if choice == "1":
    cursor.execute("SELECT * FROM rims")
    print("\n--- RIMS ---")
    for row in cursor.fetchall():
        print(row)

elif choice == "2":
    cursor.execute("SELECT * FROM tires")
    print("\n--- TIRES ---")
    for row in cursor.fetchall():
        print(row)

elif choice == "3":
    cursor.execute("SELECT * FROM tire_rim_measurements")
    print("\n--- TIRE-RIM MEASUREMENTS ---")
    for row in cursor.fetchall():
        print(row)

elif choice == "4":
    cursor.execute("SELECT * FROM motorcycle")
    print("\n--- MOTORCYCLES ---")
    for row in cursor.fetchall():
        print(row)

elif choice == "5":
    cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    AND name != 'sqlite_sequence'
    """)
    print("\n--- TABLES ---")
    for row in cursor.fetchall():
        print(row)

elif choice == "6":
    table_name = input("Enter table name: ")

    cursor.execute(f"PRAGMA table_info({table_name})")

    print(f"\n--- STRUCTURE: {table_name} ---")
    for row in cursor.fetchall():
        print(row)

else:
    print("Invalid choice.")

conn.close()