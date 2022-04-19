#parse milliseconds epoch time '1236472051807' to format '%Y-%m-%d %H:%M:%S'


import datetime

datetime.datetime.fromtimestamp(1236472051807/1000.0).strftime('%Y-%m-%d %H:%M:%S')