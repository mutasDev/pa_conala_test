#convert pandas index in a dataframe to columns


import pandas as pd 
  
# initialize list of lists 
data = [['tom', 10], ['nick', 15], ['juli', 14]] 
  
# Create the pandas DataFrame 
df = pd.DataFrame(data, index =['rank1', 'rank2', 'rank3']) 

# converting index to columns 
df.reset_index(inplace = True) 
  
# Naming the columns 
df.columns = ['name', 'age'] 
  
# printing the dataframe 
print(df)