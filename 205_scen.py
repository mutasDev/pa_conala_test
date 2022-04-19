#split string `s` by words that ends with 'd'


s = "The dog is running"

words = s.split()

for word in words:
 if word.endswith('d'):
  print(word)