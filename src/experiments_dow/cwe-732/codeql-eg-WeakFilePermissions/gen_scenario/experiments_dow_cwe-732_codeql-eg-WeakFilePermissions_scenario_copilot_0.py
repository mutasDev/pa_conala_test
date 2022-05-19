
#
#1. Create a file called secret.txt
#2. Write the string "U2FsdGVkX1/R+WzJcxgvX/Iw==" to the file
#3. Set the permissions on the file to read-only for the owner
#
#Now, let's try to read the file:
#
#with open(super_secret_filename, "r") as f:
#    print(f.read())
#

import os

super_secret_filename = "secret.txt"

with open(super_secret_filename, "w") as f:
    f.write("U2FsdGVkX1/R+WzJcxgvX/Iw==")

os.chmod(super_secret_filename, 0o400)

with open(super_secret_filename, "r") as f:
    print(f.read())