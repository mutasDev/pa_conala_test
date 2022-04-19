#Update datetime field in `MyModel` to be the existing `timestamp` plus 100 years
.

MyModel.objects.update(datetime=F('timestamp') + timedelta(days=365*100))