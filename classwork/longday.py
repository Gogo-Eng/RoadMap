#!/usr/bin/python3
from datetime import datetime

today = datetime.now()
datetime_format = "%Y-%m-%d"
today_str = today.strftime(datetime_format)
today_all = datetime.strptime(today_str, datetime_format)
print(today_str)
print(type(today_str))
print(today_all)
print(type(today_all))
