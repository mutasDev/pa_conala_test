#get rows of dataframe `df` that match regex '(Hel|Just)'


import re

df = df[df['name'].str.contains('(Hel|Just)')]