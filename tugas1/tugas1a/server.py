import sys
import socket
import threading

# Constants
CHUNK_SIZE = 64

def runServer(port):
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Bind the socket to the port
	server_address = ('localhost', port)
	print('starting up on %s port %s' % server_address)
	sock.bind(server_address)
	# Listen for incoming connections
	sock.listen(1)
	while True:
		# Wait for a connection
		print('waiting for a connection')
		connection, client_address = sock.accept()
		print('connection from %s port %s' % client_address)
		# Open file to save the data received
		file = open("../FILES/receivedbyserver.jpg", "wb")
		# Receive the data in small chunks
		received = 0
		while True:
			data = connection.recv(CHUNK_SIZE)
			received += len(data)
			print(received, len(data))
			file.write(data)
			if len(data) < CHUNK_SIZE:
				break
		# Clean up the connection
		file.close()
		print('sending status to client')
		connection.sendall(('received %d bytes' % received).encode('ascii'))
		connection.close()

port = 10000
runServer(port)
