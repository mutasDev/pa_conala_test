#Removing duplicates in list `source_list`


```
source_list = [1,1,2,2,3,3,4,4,5,5]

unique_list = []

for item in source_list:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)
```