#determine number of files on a drive with python


import os

def get_num_files(path):

num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

return num_files