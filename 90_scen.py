#removing an element from a list based on a predicate 'X' or 'N'


def remove(lst, x): 
  
    lst = [value for value in lst if value != x] 
    return lst