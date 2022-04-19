#sort list `list_of_strings` based on second index of each string `s`
 in the list.

list_of_strings = ["g", "e", "e", "k", "s"] 

list_of_strings.sort(key = lambda s: s[1]) 

print(list_of_strings)