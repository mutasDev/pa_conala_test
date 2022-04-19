#How do I INSERT INTO t1 (SELECT * FROM t2) in SQLAlchemy?


There is no direct way to do this in SQLAlchemy. However, you can create a temporary table using the Table.tometadata() method, and then use that table in your INSERT statement.

t1 = Table('t1', metadata, Column('c1', Integer), Column('c2', String))

t2 = Table('t2', metadata, Column('c1', Integer), Column('c2', String))

t1.tometadata().create()

conn.execute(t1.insert(), t2.select())