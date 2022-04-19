#loop over files in directory `source`
 and copy them to directory `destination`

import os
import shutil

source = './source/'
destination = './destination/'

for filename in os.listdir(source):
    shutil.copy(source+filename, destination)