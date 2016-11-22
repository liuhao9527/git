#!/usr/bin/python3

import re
from datetime import datetime,timedelta,timezone

def to_timestamp(dt_str):
    dt=datetime(dt_str)
    dt.timestamp()
    print(dt)
def to_datetime(str):
    dtr=datetime.strptime(str,'%Y-%m-%d %H:%M:%S')
    return dtr
t=input('the time:')
td=re.split(r'[\s\:\-]+',t)
tf=tuple(td)
if isinstance(tf,tuple):
    print('g')
else:
    print('f')
