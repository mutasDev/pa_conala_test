#find the first element of the tuple with the maximum second element in a list of tuples `lis`


```
def find_max(lis): 
    max = lis[0][1] 
    for i in range(len(lis)): 
        if lis[i][1] > max: 
            max = lis[i][1] 
    return max 
            
```