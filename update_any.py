import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("""
UPDATE motorcycle
SET front_dish_required = 1
WHERE brand = ? AND model = ?
""", ("E-ride", "Pro SS 3.0"))




conn.commit()
conn.close()

print("success.")