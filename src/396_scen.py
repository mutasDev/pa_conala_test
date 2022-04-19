#open a 'gnome' terminal from python script and run  'sudo apt-get update' command.


import subprocess

subprocess.call(["gnome-terminal", "-e", "sudo apt-get update"])