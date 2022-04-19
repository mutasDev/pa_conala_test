#get the first value from dataframe `df` where column 'Letters' is equal to 'C'


df.loc[df['Letters'] == 'C', 'Values'].iloc[0]