#get index of rows in column 'BoolCol'
 that have value 'True'

bool_col = df['BoolCol']
true_indices = [i for i, x in enumerate(bool_col) if x]