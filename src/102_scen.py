#subscript text 'H20' with '2' as subscripted in matplotlib labels for arrays 'x' and 'y'.


import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.xlabel('x (H_2O)')
plt.ylabel('y (H_2O)')

plt.plot(x, y)
plt.show()