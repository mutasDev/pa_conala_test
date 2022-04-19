#sort a list of dictionary `mylist` by the key `title`


mylist = [{'title': 'A', 'value': 1}, {'title': 'B', 'value': 2}, {'title': 'C', 'value': 3}]

mylist.sort(key=lambda x: x['title'])