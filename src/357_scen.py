#check if path `my_path` is an absolute path


import os.path

my_path = input("Enter a path: ")

if os.path.isabs(my_path):
    print("The path is absolute.")
else:
    print("The path is not absolute.")