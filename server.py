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

while True:

	Client, address = ServerSocket.accept()

	print('Connected to: ' + address[0]))

	start_new_thread(threaded_client,(Client, ))

	ThreadCount += 1

	print('Thread Number: ' + str(ThreadCount))
	
	dataFromClient = clientConnected.recv(1024)
	print(dataFromClient.decode());

ServerSocket.close()
