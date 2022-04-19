#Call a subprocess with arguments `c:\\Program Files\\VMware\\VMware Server\\vmware-cmd.bat` that may contain spaces
 in the path.

import subprocess
subprocess.call(["c:\\Program Files\\VMware\\VMware Server\\vmware-cmd.bat"])