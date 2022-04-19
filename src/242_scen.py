#Convert unix timestamp '1347517370' to formatted string '%Y-%m-%d %H:%M:%S'


import time

unix_timestamp = 1347517370

formatted_string = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(unix_timestamp))

print(formatted_string)