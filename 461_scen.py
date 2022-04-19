#How to sort a Dataframe by the ocurrences in a column in Python (pandas)


import pandas as pd

#create dataframe
df = pd.DataFrame({'col1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'col2': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4]})

#sort by column2
df.sort_values(by='col2')