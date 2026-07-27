import sqlite3

# get data from user
diameter_inch = float(input("Rim diameter [inch]: "))
width_inch = float(input("Rim width [inch]: "))
actual_width_mm = float(input("Actual rim width [mm]: "))
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
""", (diameter_inch, width_inch, actual_width_mm, notes))

# save changes
conn.commit()

# close database
conn.close()

print("Rim added sucessfully!")