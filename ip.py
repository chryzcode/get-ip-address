import socket

gethost = socket.gethostname()
ip = socket.gethostbyname(gethost)
print(f'Computer name: {gethost} ')
print(f'IP address: {ip}')
