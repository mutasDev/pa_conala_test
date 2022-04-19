#create a new column `weekday` in pandas data frame `data` based on the values in column `my_dt`


```
import pandas as pd

data['weekday'] = data['my_dt'].dt.weekday
```