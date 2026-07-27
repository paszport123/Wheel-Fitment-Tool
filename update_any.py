import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(tires)")
for column in cursor.fetchall():
    print(column[1])

# cursor.execute("""
# UPDATE tire_rim_measurements
# SET actual_tire_width_mm = 142
# WHERE tire_id = ? AND rim_id = ?
# """, ("9", "12"))

# cursor.execute("""
# ALTER TABLE motorcycle
# ADD COLUMN chain_overhang_mm REAL DEFAULT 0;
# """)

conn.commit()
conn.close()

print("success.")