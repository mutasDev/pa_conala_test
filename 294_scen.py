#unzip list `original` and return a generator
 of the unzipped elements.

original = [('a', 1), ('b', 2), ('c', 3)]

def unzip(original):
  return (i for i,j in original)