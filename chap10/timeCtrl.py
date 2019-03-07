import time

now = time.time()
print(now)

print(time.ctime(now))
print(time.localtime(now))
print(time.gmtime(now))

tm = time.localtime(now)
print(time.mktime(tm))

now = time.time()
print(time.ctime(now))

fmt = "It's %A, %B %d, %Y, local time%I:%M:%S%p"
t = time.localtime()
print(t)
print(time.strftime(fmt, t))

from datetime import date
some_day = date(2014, 7, 4)
print(some_day.strftime(fmt))

from datetime import time
some_time = time(10, 35)
print(some_time.strftime(fmt))

import time
fmt = "%Y-%m-%d"
#print(time.strptime("2012 01 29", fmt))
print(time.strptime("2012-01-29", fmt))
#print(time.strptime("2012-13-29", fmt))

