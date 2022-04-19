#get the date 7 days before the current date


import datetime

seven_days_ago = datetime.date.today() - datetime.timedelta(days=7)
print(seven_days_ago)