#get all the elements except strings from the list 'lst'.


lst = [1, 2, 'a', 'b']

new_lst = [x for x in lst if not isinstance(x, str)]

print(new_lst)