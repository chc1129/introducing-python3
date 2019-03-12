import gevent
from gevent import socket
#hosts = ['www.crappytaxidermy.com', 'www.walterpottertaxidermy,com', 'www.antique-taxidermy.com']
hosts = ['www.crappytaxidermy.com', 'www.walterpottertaxidermy.com', 'www.taxidermy.net']
jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)
