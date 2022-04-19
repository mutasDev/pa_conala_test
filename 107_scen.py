#joining data from dataframe `df1` with data from dataframe `df2` based on matching values of column 'Date_Time' in both dataframes
.

import pandas as pd

df1 = pd.DataFrame({'Date_Time': ['2018-01-01 00:00:00', '2018-01-02 00:00:00', '2018-01-03 00:00:00'],
                   'Value1': [1, 2, 3]})
df2 = pd.DataFrame({'Date_Time': ['2018-01-01 00:00:00', '2018-01-02 00:00:00', '2018-01-03 00:00:00'],
                   'Value2': [4, 5, 6]})

df = pd.mer