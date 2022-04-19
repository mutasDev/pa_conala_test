#plot dataframe `df` without a legend


import matplotlib.pyplot as plt

plt.plot(df)
plt.legend().remove()
plt.show()