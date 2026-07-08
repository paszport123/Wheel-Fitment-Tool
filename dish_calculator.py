import sqlite3

MIN_CHAIN_CLEARANCE_MM = 5

def calculate_dish(
    actual_tire_width_mm, 
    actual_width_mm
):
    
    dish = (
    (actual_tire_width_mm - actual_width_mm) / 2
    ) + MIN_CHAIN_CLEARANCE_MM

    return dish

def calculate_front_dish(
    front_fork_width_mm,
    actual_rim_width_mm,
    front_brake_surface_to_fork_mm,
    hub_machining_correction_mm = 0      
):
    zero_position = (
        front_fork_width_mm - actual_rim_width_mm
    ) / 2

    corrected_brake_surface = (
        front_brake_surface_to_fork_mm
        + hub_machining_correction_mm
    )

    front_dish = zero_position - corrected_brake_surface

    return front_dish

def brake_side_clearance(
    sprocket_surface_to_swingarm_mm, 
    actual_tire_width_mm,
    rear_swingarm_width_mm
):
    brake_side_clearance = rear_swingarm_width_mm - (
    sprocket_surface_to_swingarm_mm + 
    MIN_CHAIN_CLEARANCE_MM + actual_tire_width_mm)

    return brake_side_clearance

def sprocket_side_clearance(
    sprocket_surface_to_swingarm_mm
):
    
    sprocket_side_clearance = (
    sprocket_surface_to_swingarm_mm + MIN_CHAIN_CLEARANCE_MM)

    return sprocket_side_clearance

def choose_motorcycle(cursor):

    cursor.execute("""
    SELECT id, brand, model
    FROM motorcycle
    """)

    motorcycles = cursor.fetchall()

    print("\nAvailable motorcycles:")

    for index, motorcycle in enumerate(motorcycles, start=1):
        print(f"{index} - {motorcycle[1]} {motorcycle[2]}")

    choice = int(input("\nChoose motorcycle: "))

    selected_motorcycle_id = motorcycles[choice - 1][0]

    return selected_motorcycle_id

def choose_rim(cursor):

    cursor.execute("""
    SELECT id, diameter_inch, width_inch
    FROM rims
    """)

    rims = cursor.fetchall()

    print("\nAvailable rims:")

    for index, rim in enumerate(rims, start=1):
        print(f"{index} - {rim[1]}x{rim[2]}")

    choice = int(input("\nChoose rim: "))

    selected_rim_id = rims[choice -1][0]

    return selected_rim_id

def choose_tire(cursor, rim_id):

    cursor.execute("""
    SELECT 
        tires.id, 
        tires.brand, 
        tires.model, 
        tires.width, 
        tires.profile, 
        tires.rim_diameter_inch
    FROM tires
        JOIN tire_rim_measurements
        ON tires.id = tire_rim_measurements.tire_id
    WHERE tire_rim_measurements.rim_id = ?
    ORDER BY tires.rim_diameter_inch, tires.width, tires.profile
    """, (rim_id,))

    tires = cursor.fetchall()

    print("\nAvailable tires for selected rim:")
    print("0. No tire")

    for index, tire in enumerate(tires, start=1):
        print(
            f"{index}. "
            f"{tire[1]} {tire[2]} "
            f"{tire[3]}/{tire[4]}-{tire[5]}"
        )

    choice = int(input("\nChoose tire: "))

    if choice == 0:
        return None

    selected_tire_id = tires[choice - 1][0]

    return selected_tire_id

def get_motorcycle_data(cursor, motorcycle_id):

    cursor.execute("""
    SELECT
        rear_swingarm_width_mm,
        sprocket_surface_to_swingarm_mm,
        sprocket_adapter_offset_mm,
        front_fork_width_mm,
        front_brake_surface_to_fork_mm
    FROM motorcycle
    WHERE id = ?
    """, (motorcycle_id,))

    return cursor.fetchone()

def get_rim_data(cursor, rim_id):

    cursor.execute("""
    SELECT
        diameter_inch,
        width_inch,
        actual_width_mm
    FROM rims
    WHERE id = ?
    """, (rim_id,))

    return cursor.fetchone()

def get_tire_data(cursor, tire_id):

    cursor.execute("""
    SELECT
        brand,
        model,
        width,
        profile,
        rim_diameter_inch
    FROM tires
    WHERE id = ?
    """, (tire_id,))

    return cursor.fetchone()
    
def get_tire_rim_measurement(cursor, tire_id, rim_id):
    cursor.execute("""
    SELECT
        actual_tire_width_mm,
        actual_tire_height_mm
    FROM tire_rim_measurements
    WHERE tire_id = ?
    AND rim_id = ?
    """, (tire_id, rim_id))

    return cursor.fetchone()

# def center_wheel(
#     dish,
#     brake_side_clearance,
#     sprocket_side_clearance
# ):




# Connect to database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# choose dish type
print("\n---DISH CALCULATOR---")
print("#1 Rear dish")
print("#2 Front dish")

dish_type = input("Choose dish type: ")

if dish_type == "1":

    motorcycle_id = choose_motorcycle(cursor)
    rim_id = choose_rim(cursor)
    tire_id = choose_tire(cursor, rim_id)

    motorcycle_data = get_motorcycle_data(cursor, motorcycle_id)
    rim_data = get_rim_data(cursor, rim_id)
    # tire_data = get_tire_data(cursor, tire_id)
    # measurement_data = get_tire_rim_measurement(cursor, tire_id, rim_id)

    rear_swingarm_width_mm = motorcycle_data[0]
    sprocket_surface_to_swingarm_mm = motorcycle_data[1]
    sprocket_adapter_offset_mm = motorcycle_data[2]

    diameter_inch = rim_data[0]
    width_inch = rim_data[1]
    actual_rim_width_mm = rim_data[2]

    if tire_id is None:
        
        actual_tire_width_mm = actual_rim_width_mm

    else:
        
        tire_data = get_tire_data(cursor, tire_id)
        measurement_data = get_tire_rim_measurement(cursor, tire_id, rim_id)

        brand = tire_data[0]
        model = tire_data[1]

        actual_tire_width_mm = measurement_data[0]
        actual_tire_height_mm = measurement_data[1]

# print("\n---RESULT---")
# print(f"Dish: {dish} mm")

# print("\n---DEBUG---")
# print(motorcycle_data)
# print(rim_data)
# print(tire_data)
# print(measurement_data)

    dish = calculate_dish(
        actual_tire_width_mm,
        actual_rim_width_mm
    )

    final_dish = dish - sprocket_adapter_offset_mm

    brake_side_clearance = brake_side_clearance(
        sprocket_surface_to_swingarm_mm, 
        actual_tire_width_mm,
        rear_swingarm_width_mm
    )

    sprocket_side_clearance = sprocket_side_clearance(
        sprocket_surface_to_swingarm_mm
    )

    if brake_side_clearance > sprocket_side_clearance:

        wheel_centering = (brake_side_clearance - sprocket_side_clearance) / 2

    else:

        wheel_centering = 0

    print("before corrections")
    print(f"Dish: {dish} mm")
    print(f"brake_side_clearance: {brake_side_clearance} mm")
    print(f"sprocket_side_clearance: {sprocket_side_clearance} mm")

    if sprocket_adapter_offset_mm > 0:
        print(
            f"Sprocket adapter correction: "
            f"-{sprocket_adapter_offset_mm} mm"
        )
        print(
            f"(---Final dish---) measured without adapter: "
            f"{final_dish + wheel_centering} mm"
        )
    else:
        print(f"(---Final dish---): {dish + wheel_centering} mm")

    if wheel_centering > 0:
        print("after wheel centering")
        print(f"brake_side_clearance: {brake_side_clearance - wheel_centering} mm")
        print(f"sprocket_side_clearance: {sprocket_side_clearance + wheel_centering} mm")
    else:
        print("...")

elif dish_type == "2":
    motorcycle_id = choose_motorcycle(cursor)
    rim_id = choose_rim(cursor)

    motorcycle_data = get_motorcycle_data(cursor, motorcycle_id)
    rim_data = get_rim_data(cursor, rim_id)

    front_fork_width_mm = motorcycle_data[3]
    front_brake_surface_to_fork_mm = motorcycle_data[4]
    actual_rim_width_mm = rim_data[2]

    hub_machining_correction_mm = float(
        input("\nHub machining correction [mm]: ")
    )

    front_dish = calculate_front_dish(
        front_fork_width_mm,
        actual_rim_width_mm,
        front_brake_surface_to_fork_mm,
        hub_machining_correction_mm
    )

    print(f"\nFront dish: {front_dish:.1f} mm")

else:
    print("Invalid choice.")
    

conn.close()