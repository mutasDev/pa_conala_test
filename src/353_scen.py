#find duplicate names in column 'name' of the dataframe `x`


```
import pandas as pd

x = pd.DataFrame({'name': ['John', 'Mary', 'John', 'Mike', 'Mike']})

duplicated_names = x['name'].duplicated()

print(x[duplicated_names])
```