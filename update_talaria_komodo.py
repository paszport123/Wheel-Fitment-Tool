import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("""
UPDATE motorcycle
SET front_brake_surface_to_fork_mm = 13
WHERE brand = ? AND model = ?
""", ("Talaria", "Komodo"))




conn.commit()
conn.close()

print("success.")