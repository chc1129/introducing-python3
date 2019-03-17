import socket
print(socket.gethostbyname('www.crappytaxidermy.com'))
print(socket.gethostbyname_ex('www.crappytaxidermy.com'))

print(socket.getaddrinfo('www.crappytaxidermy.com', 80))

print(socket.getaddrinfo('www.crappytaxidermy,com', 80, socket.AF_INET, socket.SOCK_STREAM))
