#execute script 'script.ps1' using 'powershell.exe' shell
.

import subprocess

subprocess.call(["powershell.exe", "script.ps1"])