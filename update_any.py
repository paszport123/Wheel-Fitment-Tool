import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("""
UPDATE motorcycle
SET chain_overhang_mm = 5
WHERE brand = ? AND model = ?
""", ("Sur-Ron", "Light Bee"))

# cursor.execute("""
# ALTER TABLE motorcycle
# ADD COLUMN chain_overhang_mm REAL DEFAULT 0;
# """)

conn.commit()
conn.close()

print("success.")