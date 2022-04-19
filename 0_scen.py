#send a signal `signal.SIGUSR1` to the current process
.

import signal
signal.signal(signal.SIGUSR1, lambda signum, frame: print('Received SIGUSR1'))