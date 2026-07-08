# import sqlite3

# conn = sqlite3.connect("database.db")
# cursor = conn.cursor()


# cursor.execute("""
# UPDATE motorcycle
# SET
#     front_fork_width_mm = ?,
#     front_brake_surface_to_fork_mm = ?
# WHERE id = ?
# """, (118, 14, 2))


# conn.commit()
# conn.close()

# print("success.")