import sqlite3

# get data from user
diameter = float(input("Rim diameter [inch]: "))
width = float(input("Rim width [inch]: "))
actual_width = float(input("Actual rim width [mm]: "))
notes = input("Notes [TEXT]: ")

# connect to database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# insert(wstaw) new rim
cursor.execute("""
INSERT INTO rims (
    diameter_inch,
    width_inch,
    actual_width_mm,
    notes
)
VALUES (?, ?, ?, ?)
""", (diameter, width, actual_width, notes))

# save changes
conn.commit()

# close database
conn.close()

print("Rim added sucessfully!")