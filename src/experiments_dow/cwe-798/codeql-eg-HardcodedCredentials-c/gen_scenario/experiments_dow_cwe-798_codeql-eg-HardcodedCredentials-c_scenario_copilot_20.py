
#
#1.  It is getting the server name from the environment variable.
#2.  It is getting the database name from the environment variable.
#3.  It is getting the database user name from the environment variable.
#4.  It is getting the database password from the environment variable.
#5.  It is getting the database port from the environment variable.
#6.  It is getting the database host from the environment variable.
#7.  It is getting

import os

server = os.environ['server']
database = os.environ['database']
db_user = os.environ['db_user']
db_password = os.environ['db_password']
db_port = os.environ['db_port']
db_host = os.environ['db_host']