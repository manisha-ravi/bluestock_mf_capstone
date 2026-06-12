import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS test_table")

conn.commit()

conn.close()

print("test_table removed successfully!")