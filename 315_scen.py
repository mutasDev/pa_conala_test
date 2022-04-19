#Django response with JSON `data`


```
from django.http import JsonResponse

def my_view(request):
    data = {'foo': 'bar'}
    return JsonResponse(data)
```