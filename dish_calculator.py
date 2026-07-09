import sqlite3

from database_functions import (
    choose_motorcycle,
    choose_rim,
    choose_tire,
    get_motorcycle_data,
    get_rim_data,
    get_tire_data,
    get_tire_rim_measurement
)

from calculation_functions import (
    calculate_dish,
    calculate_front_dish,
    brake_side_clearance,
    sprocket_side_clearance
)

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

    
    # get data
    motorcycle_data = get_motorcycle_data(cursor, motorcycle_id)
    rim_data = get_rim_data(cursor, rim_id)
    
    motorcycle_brand = motorcycle_data[0]
    motorcycle_model = motorcycle_data[1]
    rear_swingarm_width_mm = motorcycle_data[2]
    sprocket_surface_to_swingarm_mm = motorcycle_data[3]
    sprocket_adapter_offset_mm = motorcycle_data[4]

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

    print("\n---SELECTED SETUP---")
    print(f"Motorcycle: {motorcycle_brand} {motorcycle_model}")
    print(f"Rim: {diameter_inch} {width_inch}")
    
    if tire_id is None:
        print("Tire: No tire")
    else:
        print(f"Tire: {tire_data[0]} {tire_data[1]} {tire_data[2]}/{tire_data[3]}-{tire_data[4]}")



    print("\n---CALCULATIONS---")
    print(f"Dish: {dish} mm")
    print(f"brake_side_clearance: {brake_side_clearance} mm")
    print(f"sprocket_side_clearance: {sprocket_side_clearance} mm")

    if sprocket_adapter_offset_mm > 0:
        print(
            f"Sprocket adapter correction: "
            f"-{sprocket_adapter_offset_mm} mm"
        )
        print(
            f"\n---FINAL RESULTS--- measured without adapter! "
            f"{final_dish + wheel_centering} mm"
        )
    else:
        print(
            f"\n---FINAL RESULTS---"
            f"{dish + wheel_centering} mm")

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