#Removing duplicates in list `abracadabra`


abracadabra = ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']

seen = set()
result = []
for item in abracadabra:
    if item not in seen:
        seen.add(item)
        result.append(item)

print(result)