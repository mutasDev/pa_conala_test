#Insert directory 'apps' into directory `__file__`


import os

directory = os.path.dirname(__file__)
directory = os.path.join(directory, 'apps')

if not os.path.exists(directory):
    os.makedirs(directory)