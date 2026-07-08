import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# PONIZEJ UTWORZONA ZOSTALA BAZA DANCYH
# JEST UTWORZONY WIEC TEGO FRAGMENTU JUZ NIE POTRZEBUJE ZEBY NIE TWORZYL SIE ZA KAZDYM RAZEM NA NOWO

# RIMS
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS rims (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     diameter_inch INTEGER NOT NULL,
#     width_inch REAL NOT NULL,
#     actual_width_mm INTEGER NOT NULL,
#     notes TEXT
# )
# """)

# TIRES
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS tires (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     brand TEXT NOT NULL,
#     model TEXT NOT NULL,
#     width INTEGER NOT NULL,
#     profile INTEGER NOT NULL,
#     rim_diameter_inch REAL NOT NULL,
#     notes TEXT
# )
# """)

#TIRE RIM
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS tire_rim_measurements (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     tire_id INTEGER NOT NULL,
#     rim_id INTEGER NOT NULL,
#     actual_tire_width_mm INTEGER NOT NULL,
#     actual_tire_height_mm INTEGER NOT NULL,
#     notes TEXT
# )
# """)

#MOTORCYCLE
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS motorcycle (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     brand TEXT NOT NULL,
#     model TEXT NOT NULL,
#     rear_swingarm_width_mm INTEGER NOT NULL,
#     sprocket_surface_to_swingarm_mm INTEGER NOT NULL,
#     notes TEXT
# )
# """)

# conn.commit()
# conn.close()

