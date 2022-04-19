#Python Pandas: How to replace a characters in a column of a dataframe?


In [1]: df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
   ...:                           'foo', 'bar', 'foo', 'foo'],
   ...:                    'B': ['one', 'one', 'two', 'three',
   ...:                           'two', 'two', 'one', 'three'],
   ...:                    'C': np.random.randn(8),
   ...:                    'D': np.random.randn(8)})
   ...: 

In [2]: df
Out[2]: 
     A      B         C         D
