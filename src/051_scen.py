#convert epoch time represented as milliseconds `s` to string using format '%Y-%m-%d %H:%M:%S.%f'


```
import time

def convert_ms_to_string(s):
  return time.strftime('%Y-%m-%d %H:%M:%S.%f', time.localtime(s/1000.0))
```