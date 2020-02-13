import sys
import socket

# Constants
CHUNK_SIZE = 64
PORT = 10000

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', PORT)
print ('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    # Sending request for a file
    msg = '../FILES/tobesent.jpg'.encode('ascii')
    sock.sendall(msg)
    print('File request has sent.')

    # Start receiving chunks from server and save to receivedbyclient.jpg
    file = open('../FILES/receivedbyclient.jpg', "wb")
    received = 0
    while True:
        chunk = sock.recv(CHUNK_SIZE)
        if chunk:
            received += len(chunk)
            file.write(chunk)
            print(f'Received: {received} bytes.')
        else:
            print('No more data received.')
            break
    print('Request completed.')
    file.close()
finally:
    print ('closing socket')
    sock.close()
