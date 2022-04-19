#rotate the xtick labels of matplotlib plot `ax` by `45` degrees to make long labels readable
.

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

for tick in ax.get_xticklabels():
    tick.set_rotation(45)

plt.show()