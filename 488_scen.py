#get a list of all keys in Cassandra database `cf` with pycassa


from pycassa.system_manager import *

cf = ColumnFamily(pool, 'cf')

for key in cf.get_range():
   print key