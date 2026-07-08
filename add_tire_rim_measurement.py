import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Show tires
print("\nAvailable tires:")
cursor.execute("""
SELECT id, brand, model, width, profile, rim_diameter_inch
FROM tires
""")

for tire in cursor.fetchall():
    print(f"{tire[0]} - {tire[1]} {tire[2]} {tire[3]}/{tire[4]}-{tire[5]}")

tire_id = int(input("\nChoose tire ID: "))

# Show rims
print("\nAvailable rims:")
cursor.execute("""
SELECT id, diameter_inch, width_inch, actual_width_mm
FROM rims
""")

for rim in cursor.fetchall():
    print(f"{rim[0]} - {rim[1]}x{rim[2]}")

rim_id = int(input("\nChoose rim ID: "))

# Add measurement
actual_tire_width = float(input("Actual tire width [mm]: "))
actual_tire_height = float(input("Actual tire height [mm]: "))
notes = input("Notes: ")

cursor.execute("""
INSERT INTO tire_rim_measurements (
    tire_id,
    rim_id,
    actual_tire_width_mm,
    actual_tire_height_mm,
    notes
)
VALUES (?, ?, ?, ?, ?)
""", (
    tire_id,
    rim_id,
    actual_tire_width,
    actual_tire_height,
    notes
))

conn.commit()
conn.close()

print("Tire-rim measurement added successfully.")