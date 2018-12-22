h = 60 #min
m = 60 #sec
d = 24 #hour
seconds_per_hour = (h * m)
seconds_per_day = (d * seconds_per_hour)
result = (seconds_per_day // seconds_per_hour)
print(result)
