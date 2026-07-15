import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("""
UPDATE motorcycle
SET front_fork_width_mm = 114
WHERE brand = ? AND model = ?
""", ("Talaria", "Komodo"))




conn.commit()
conn.close()

print("success.")