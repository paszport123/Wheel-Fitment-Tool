import sqlite3

# Get data from user
brand = input("Motorcycle brand: ")
model = input("Motorcycle model: ")

rear_swingarm_width = float(input("Rear swingarm width [mm]: "))
sprocket_surface_to_swingarm = float(input("Sprocket surface to swingarm [mm]: "))
sprocket_adapter_offset_mm = float(input("sprocket adapter offset [mm]: "))

front_fork_width_mm = float(input("Front fork width at axle [mm]: "))
front_brake_surface_to_fork_mm = float(input("Front brake surface to fork [mm]: "))
minimum_chain_clearance_mm = float(input("minimum chain clearance (5mm + ((chain width - sprocket width) / 2) [mm]"))

notes = input("Notes: ")

# Connect to database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Insert new motorcycle
cursor.execute("""
INSERT INTO motorcycle (
    brand,
    model,
    rear_swingarm_width_mm,
    sprocket_surface_to_swingarm_mm,
    sprocket_adapter_offset_mm,
    front_fork_width_mm,
    front_brake_surface_to_fork_mm,
    minimum_chain_clearance_mm,
    notes
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", (
    brand,
    model,
    rear_swingarm_width,
    sprocket_surface_to_swingarm,
    sprocket_adapter_offset_mm,
    front_fork_width_mm,
    front_brake_surface_to_fork_mm,
    notes
))

# Save changes
conn.commit()

# Close database
conn.close()

print("Motorcycle added successfully.")