import sqlite3

# Get data from user
brand = input("Motorcycle brand: ")
model = input("Motorcycle model: ")

# ---REAR WHEEL---
rear_swingarm_width_mm = float(input("Rear swingarm width [mm]: "))
sprocket_surface_to_swingarm_mm = float(input("Sprocket surface to swingarm [mm]: "))
sprocket_adapter_offset_mm = float(input("Sprocket adapter offset [mm]: "))
chain_overhang_mm = float(input("Chain overhang [mm]: "))
# minimum_chain_clearance_mm = float(input("minimum chain clearance (5mm + ((chain width - sprocket width) / 2) [mm]"))

# ---FRONT WHEEL---
front_dish_required = int(input("Is the front dish required? (1-Yes, 0-No)"))

if front_dish_required is 1:
    front_fork_width_mm = float(input("Front fork width at axle [mm]: "))
    front_brake_surface_to_fork_mm = float(input("Front brake surface to fork [mm]: "))

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
    notes,
    sprocket_adapter_offset_mm,
    front_fork_width_mm,
    front_brake_surface_to_fork_mm,
    front_dish_required,
    minimum_chain_clearance_mm,
    chain_overhang_mm
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    brand,
    model,
    rear_swingarm_width_mm,
    sprocket_surface_to_swingarm_mm,
    notes,
    sprocket_adapter_offset_mm,
    front_fork_width_mm,
    front_brake_surface_to_fork_mm,
    front_dish_required,
    # minimum_chain_clearance_mm,
    chain_overhang_mm
))

# Save changes
conn.commit()

# Close database
conn.close()

print("Motorcycle added successfully.")