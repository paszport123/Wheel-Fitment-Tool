import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("""
UPDATE motorcycle
SET sprocket_surface_to_swingarm_mm = -9
WHERE brand = ? AND model = ?
""", ("Talaria", "Komodo"))




conn.commit()
conn.close()

print("success.")