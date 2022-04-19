#Create a list containing the indexes of rows where the value of column 'BoolCol' in dataframe `df` are equal to True


bool_indexes = df[df['BoolCol']].index.tolist()