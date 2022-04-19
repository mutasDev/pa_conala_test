#write records in dataframe `df` to table 'test' in schema 'a_schema'
 in database 'my_database'

```
import pandas as pd

# Connect to database
conn = psycopg2.connect(dbname='my_database', user='my_user', host='my_host', port='my_port')

# Write records in dataframe to table
df.to_sql('test', schema='a_schema', con=conn, if_exists='replace', index=False)

# Close connection
conn.close()
```