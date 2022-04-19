#django filter by hour


This code will filter by hour:

import datetime

from django.db.models import Q

def filter_by_hour(queryset, hour):

return queryset.filter(

Q(start_time__hour=hour) |

Q(end_time__hour=hour)

)