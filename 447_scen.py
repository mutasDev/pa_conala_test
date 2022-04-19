#decode json string `request.body` to python dict


```
import json

def decode_request_body(request):
    try:
        return json.loads(request.body)
    except:
        return None
```