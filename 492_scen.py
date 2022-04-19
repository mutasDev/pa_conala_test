#choose a random file from the directory contents of the C drive, `C:\\`


import os
import random

def main():
    path = 'C:\\'
    files = os.listdir(path)
    index = random.randrange(0, len(files))
    print(files[index])

if __name__ == "__main__":
    main()