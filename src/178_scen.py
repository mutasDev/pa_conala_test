#create a DatetimeIndex containing 13 periods of the second friday of each month starting from date '2016-01-01'


import pandas as pd

start_date = '2016-01-01'
end_date = '2019-01-01'

date_range = pd.date_range(start=start_date, end=end_date, freq='2MS')

date_range