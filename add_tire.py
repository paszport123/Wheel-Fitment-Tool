import sqlite3

# Get data from user
brand = input("Tire brand: ")
model = input("Tire model: ")

width = float(input("Tire width [mm]: "))
profile = float(input("Tire profile: "))
rim_diameter = float(input("Rim diameter [inch]: "))

notes = input("Notes: ")

# Connect to database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Insert new tire
cursor.execute("""
INSERT INTO tires (
    brand,
    model,
    width,
    profile,
    rim_diameter_inch,
    notes
)
VALUES (?, ?, ?, ?, ?, ?)
""", (
    brand,
    model,
    width,
    profile,
    rim_diameter,
    notes
))

# Save changes
conn.commit()

# Close database
conn.close()

print("Tire added successfully.")