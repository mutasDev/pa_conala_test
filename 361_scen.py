#split a list in first column  into multiple columns keeping other columns as well in pandas data frame


import pandas as pd

df = pd.read_csv('file.csv')

df_split = df['column1'].str.split(',', expand=True)

df_split.columns = ['column1_1', 'column1_2', 'column1_3']

df = df.join(df_split)

df.drop('column1', axis=1, inplace=True)