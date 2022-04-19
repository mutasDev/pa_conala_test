#Sort a list of dictionaries `list_to_be_sorted` by the value of the dictionary key `name`


list_to_be_sorted = [{'name': 'A', 'value': 10}, {'name': 'B', 'value': 1}, {'name': 'C', 'value': 22}]

list_to_be_sorted.sort(key=lambda x: x['name'])