#filter rows in pandas starting with alphabet 'f' using regular expression.


import pandas as pd 
  
# Read the CSV file 
df = pd.read_csv("sample_data.csv") 
  
# Use filter to select rows 
# starting with 'f' 
df.filter(regex = '^f', axis = 0)