import sqlite3

conn = sqlite3.connect("application.db")
cur = conn.cursor()

cur.execute("SELECT id, firstname, lastname, course, start_year, start_month, reg_number, reg_date FROM application;")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()