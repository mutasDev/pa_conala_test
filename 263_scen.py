#sort a list of dictionaries by the value of keys 'title', 'title_url', 'id' in ascending order.


l = [{'title': 'A', 'title_url': 'a', 'id': 1}, {'title': 'B', 'title_url': 'b', 'id': 2}, {'title': 'C', 'title_url': 'c', 'id': 3}]

l.sort(key=lambda d: (d['title'], d['title_url'], d['id']))