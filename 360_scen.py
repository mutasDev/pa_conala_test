#pandas dataframe get first row of each group by 'id'


import pandas as pd

df = pd.DataFrame({'id':[1,2,3,4,5,6], 'name':['A','B','C','D','E','F'], 'value':[10,20,30,40,50,60]})

df.groupby('id').first()