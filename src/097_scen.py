#convert a string into datetime using the format '%Y-%m-%d %H:%M:%S.%f'


import datetime

date_string = '2018-06-29 08:15:27.243860'
date_datetime = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f')