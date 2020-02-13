import sys
import socket
import threading

# Constants
CHUNK_SIZE = 64
PORT = 10000

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

		# Receive the request
		request = connection.recv(CHUNK_SIZE)

		# Parse the requested file
		file = open(request.decode('ascii'), "rb")
		print('Send the requested file.')
		while True:
			chunk = file.read(CHUNK_SIZE)
			if len(chunk) <= 0:
				break
			connection.sendall(chunk)
		print('Sending file completed.')
		# Clean up the connection
		file.close()
		connection.close()

runServer(PORT)
