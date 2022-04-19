#call multiple bash function ‘vasp’ and ‘tee tee_output’ using ‘|’


import subprocess

subprocess.call(["vasp", "tee", "tee_output"], shell=True)