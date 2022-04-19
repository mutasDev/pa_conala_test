#replace all occurences of newlines `\n` with `<br>` in dataframe `df`


for i in range(len(df)):
  df.iloc[i,0] = df.iloc[i,0].replace('\n','<br>')