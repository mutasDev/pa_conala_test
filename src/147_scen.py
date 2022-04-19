#insert data from a string `testfield` to sqlite db `c`


```
import sqlite3

conn = sqlite3.connect('c:\\test.db')
c = conn.cursor()

c.execute("INSERT INTO testfield VALUES ('testfield')")

conn.commit()
conn.close()
```