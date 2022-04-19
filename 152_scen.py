#scatter a plot with x, y position of `np.random.randn(100)` and face color equal to none
.

import matplotlib.pyplot as plt

x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y, facecolor='none')
plt.show()