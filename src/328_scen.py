#plotting stacked barplots on a panda data frame


import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'A': [1,2,3], 'B': [4,5,6], 'C': [7,8,9]})

df.plot.bar(stacked=True)

plt.show()