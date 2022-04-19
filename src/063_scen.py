#Insert a 'None' value into a SQLite3 table.


conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("INSERT INTO table_name VALUES (NULL, 'value1', 'value2')")

conn.commit()
conn.close()