#Create new DataFrame object by merging columns "key" of  dataframes `split_df` and `csv_df` and rename the columns from dataframes `split_df` and `csv_df` with suffix `_left` and `_right` respectively
.

```
import pandas as pd

split_df = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                     'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
   
csv_df = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                          'B': ['B0', 'B1', 'B2']})

new_df = pd.merge(split_df, csv_df