#make a barplot of data in column `group` of dataframe `df` colour-coded according to list `color`


```
import matplotlib.pyplot as plt

plt.bar(df['group'], df['value'], color=color)
plt.show()
```