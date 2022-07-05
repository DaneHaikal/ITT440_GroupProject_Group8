import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = ''
port = 8889
ThreadCount = 0

try:
	ServerSocket.bind((host,port))
except socket.error as e:
	print(str(e))

print('Waiting for a Connection...')

ServerSocket.listen(5)
