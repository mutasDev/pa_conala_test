#find the key associated with the largest value in dictionary `x` whilst key is non-zero value


x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

max_value = max(x.values()) 
  
for key, value in x.items(): 
    if value == max_value and value != 0: 
        print(key)