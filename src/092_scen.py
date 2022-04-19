#count non zero values in each column in pandas data frame


import pandas as pd 
  
# initialize list of lists 
data = [[0, 1, 2, 0], [3, 4, 5, 0], [6, 7, 8, 0]] 
  
# Create the pandas DataFrame 
df = pd.DataFrame(data, columns = ['A', 'B', 'C', 'D']) 
  
# print dataframe. 
df 

# column wise count of non zero values 
df.apply(lambda x: x.count(), axis = 0)