#get rid of None values in dictionary `kwargs`


kwargs = {'key1': 'value1', 'key2': 'value2', 'key3': None}

kwargs = {k: v for k, v in kwargs.items() if v is not None}