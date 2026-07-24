import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("""
UPDATE motorcycle
SET sprocket_surface_to_swingarm_mm = -4.5
WHERE brand = ? AND model = ?
""", ("Talaria", "Komodo"))

# cursor.execute("""
# ALTER TABLE motorcycle
# ADD COLUMN chain_overhang_mm REAL DEFAULT 0;
# """)

conn.commit()
conn.close()

print("success.")