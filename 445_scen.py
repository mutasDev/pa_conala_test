#How to create a list of date string in 'yyyymmdd' format with Python Pandas?


import pandas as pd 

dates = pd.date_range('20200101', periods=10).tolist()

date_strings = [date.strftime('%Y%m%d') for date in dates]

print(date_strings)