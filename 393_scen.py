#Convert  DateTime column 'date' of pandas dataframe 'df' to ordinal
 datetime

import pandas as pd

df['date'] = pd.to_datetime(df['date']).apply(lambda x: x.toordinal())