#Format a datetime string `when` to extract date only


import datetime

when = datetime.datetime.now()
date_only = when.strftime("%m/%d/%Y")