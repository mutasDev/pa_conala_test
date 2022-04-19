#check if a directory `path` exists and create it if necessary
.

import os

if not os.path.exists(path):
    os.makedirs(path)