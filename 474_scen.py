#convert a urllib unquoted string `unescaped` to a json data `json_data`


import json

unescaped = urllib.unquote(unescaped)
json_data = json.loads(unescaped)