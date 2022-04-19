#how to get a single result from a SQLite query in python?


conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute('SELECT * FROM stocks WHERE symbol=?', 'AAPL')

print(c.fetchone())