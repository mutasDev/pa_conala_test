#check if directory `directory ` exists and create it if necessary
.

import os

directory = 'directory'

if not os.path.exists(directory):
    os.makedirs(directory)