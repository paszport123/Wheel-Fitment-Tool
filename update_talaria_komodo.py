# import sqlite3

# conn = sqlite3.connect("database.db")
# cursor = conn.cursor()


# cursor.execute("""
# UPDATE motorcycle
# SET rear_swingarm_width_mm = ?
# WHERE brand = ? AND model = ?
# """, (
#     198,
#     "Talaria",
#     "Komodo"
# ))


# conn.commit()
# conn.close()

# print("success.")