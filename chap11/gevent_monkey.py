import gevent
from gevent import monkey; monkey.patch_all()
import socket
hosts = ['www.crappytaxidermy.com', 'www.walterpottertaxidermy.com', 'www.taxidermy.net']
jobs = [gevent.spawn(socket.gethostbyname, host) for host in hosts]
for job in jobs:
    print(job.value)
