#get list of indexes of rows where column 'BoolCol' values match True


bool_col = df['BoolCol']
true_indexes = [i for i, x in enumerate(bool_col) if x]