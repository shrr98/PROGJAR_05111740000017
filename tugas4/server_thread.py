from socket import *
import socket
import threading
import time
import sys

from protocol import Protocol

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        self.protocol = Protocol()
        threading.Thread.__init__(self)

    def run(self):
        pkt = ''
        while True:
            print('1')
            data = self.connection.recv(32)
            if data:
                pkt += data.decode()
                print(pkt)
            else:
                break
        hasil = self.protocol.proses(pkt)
        print(hasil)
        self.connection.sendall(hasil.encode())
        print('sukses send')
        self.connection.close()
        
class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', 10000))
        self.my_socket.listen(1)
        while True:
            self.connection, self.client_address = self.my_socket.accept()

            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)


def main():
    svr = Server()
    svr.start()


if __name__ == "__main__":
    main()

