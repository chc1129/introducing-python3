import socket

print(socket.getaddrinfo('www.crappytaxidermy.com', 80))

print(socket.getaddrinfo('www.crappytaxidermy.com', 80, socket.AF_INET, socket.SOCK_STREAM))
