#run script 'hello.py' with argument 'htmlfilename.htm' on terminal using python executable


import subprocess

subprocess.call(["python", "hello.py", "htmlfilename.htm"])