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
    powdercoated_correction = 0,
    hub_machining_correction_mm = 0
):
    
    corrected_rim_width = actual_rim_width_mm + powdercoated_correction

    zero_position = (
        front_fork_width_mm - corrected_rim_width
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