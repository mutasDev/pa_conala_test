#Find all files in directory "/mydir" with extension ".txt"


import os

directory = "/mydir"

for filename in os.listdir(directory):
  if filename.endswith(".txt"):
    print(os.path.join(directory, filename))