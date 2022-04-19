#sort a list of dictionaries `l` by values in key `name` in descending order
.

l.sort(key=lambda x: x['name'], reverse=True)