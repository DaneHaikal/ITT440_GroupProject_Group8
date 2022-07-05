import socket

ClientSocket = socket.socket()
host = '192.168.56.109'
port = 8889

print ('Waiting for Connection...')

try:

	ClientSocket.connect((host, port))

except socket.error as e:

	print(str(e))

