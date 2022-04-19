#find a value within nested json 'data' where the key inside another key 'B' is unknown.


import json data = { "A": { "B": { "C": "D" } } } def find(key, dictionary): for k, v in dictionary.items(): if k == key: yield v elif isinstance(v, dict): for result in find(key, v): yield result if __name__ == "__main__": for result in find("C", data): print(result)