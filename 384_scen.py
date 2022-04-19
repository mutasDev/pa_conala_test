#fetch address information for host 'google.com' ion port 80


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("google.com", 80))
print(s.getsockname())
s.close()