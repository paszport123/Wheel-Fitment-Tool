import sqlite3

def choose_motorcycle(cursor, dish_type):

    if dish_type == "2":
        cursor.execute("""
            SELECT id, brand, model
            FROM motorcycle
            WHERE front_dish_required = 1
            ORDER BY brand, model
        """)
    else:
        cursor.execute("""
            SELECT id, brand, model
            FROM motorcycle
            ORDER BY brand, model
        """)

    motorcycles = cursor.fetchall()

    print("\nAvailable motorcycles:")

    for index, motorcycle in enumerate(motorcycles, start=1):
        print(f"{index} - {motorcycle[1]} {motorcycle[2]}")

    while True:
        try:
            choice = int(input("\nChoose motorcycle: "))

            if 1 <= choice <= len(motorcycles):
                return motorcycles[choice - 1][0]

            print("Invalid number. Try again.")

        except ValueError:
            print("Please enter a number.")

def choose_rim(cursor):

    cursor.execute("""
    SELECT id, diameter_inch, width_inch
    FROM rims
    """)

    rims = cursor.fetchall()

    print("\nAvailable rims:")

    for index, rim in enumerate(rims, start=1):
        print(f"{index} - {rim[1]}x{rim[2]}")

    while True:
        try:
            choice = int(input("\nChoose rim: "))

            if 1 <= choice <= len(rims):
                return rims[choice - 1][0]

            print("Invalid number. Try again.")

        except ValueError:
            print("Please enter a number.")

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

    while True:
        try:
            choice = int(input("\nChoose tire: "))

            if choice == 0:
                return None

            if 1 <= choice <= len(tires):
                return tires[choice - 1][0]

            print("Invalid number. Try again.")

        except ValueError:
            print("Please enter a number.")

def get_motorcycle_data(cursor, motorcycle_id):

    cursor.execute("""
    SELECT
        brand,
        model,           
        rear_swingarm_width_mm,
        sprocket_surface_to_swingarm_mm,
        sprocket_adapter_offset_mm,
        front_fork_width_mm,
        front_brake_surface_to_fork_mm,
        chain_overhang_mm
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