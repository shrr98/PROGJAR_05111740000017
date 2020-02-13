import sys
import socket

# Constants
CHUNK_SIZE = 64

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print ('connecting to %s port %s' % server_address)
sock.connect(server_address)


try:
    # Parse file
    file = open("../FILES/tobesent.jpg", "rb")
    # Send data as chunks
    print('Start to send File')
    while True:
        chunk = file.read(CHUNK_SIZE)
        if len(chunk) <= 0:
            break
        sock.sendall(chunk)
    print('File has been sent to server completely.')
    respon = sock.recv(16)
    print ('Status: "%s"' % respon.decode('ascii'))
    file.close()
finally:
    print ('closing socket')
    sock.close()
