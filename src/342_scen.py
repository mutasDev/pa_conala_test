#unpack a series of tuples in pandas into a DataFrame with column names 'out-1' and 'out-2'


import pandas as pd

tuples = [('out-1', 'out-2'), ('out-3', 'out-4'), ('out-5', 'out-6')]

df = pd.DataFrame(tuples, columns=['out-1', 'out-2'])