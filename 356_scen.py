#place the radial ticks in plot `ax` at 135 degrees


import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.set_theta_direction(-1)
ax.set_theta_zero_location("S")

plt.show()