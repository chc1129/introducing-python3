with open('today.txt', 'rt') as input:
    today_string = input.read()

print(today_string)

import time

fmt = '%Y-%m-%d\n'
print(time.strptime(today_string, fmt))
