#get a value of datetime.today() in the UTC time zone


import datetime

datetime.datetime.today().replace(tzinfo=datetime.timezone.utc)