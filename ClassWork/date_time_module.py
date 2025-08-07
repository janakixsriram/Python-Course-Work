from datetime import date,time,datetime,timedelta

today = date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())

"""
1 - monday  (iso) 0 - monday
7 - saturday    6 - sunday
"""

d = date(2003,9,19)
print(d)
p = date(2003,11,19) 
print(p)

"""working with time"""

t = time(23,59,12)
print(t)


now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

"""Formatting Examples using strf(string format)"""

print(now.strftime("%Y-%m-%d"))
print(now.strftime("%H:%M:%S"))
print(now.strftime("%d-%b-%Y %I:%M %p"))

"""time delta"""

fdate = today + timedelta(days = 7)
print(fdate)

pdate = today - timedelta(days = 7)
print(pdate)

fmins = now + timedelta(hours = 2)
print(fmins)

pmins = now - timedelta(hours = 2)
print(pmins)

