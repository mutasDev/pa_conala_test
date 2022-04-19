#get the largest key whose not associated with value of 0 in dictionary `x`


x = {1:5, 2:0, 3:6, 4:0}

max_key = max(x, key=lambda k: x[k] != 0)
print(max_key)