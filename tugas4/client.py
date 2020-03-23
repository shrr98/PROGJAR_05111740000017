import sys
import os
import socket
import logging
import json
from base64 import b64decode, b64encode

def list():
    data = {}
    data["cmd"] = "list"
    msg = json.dumps(data)
    pkt_str = kirim_data(msg)
    pkt = json.loads(pkt_str)
    print('---------------')
    print(f"RESPONS: {pkt['res']}")
    if(pkt['res']=='OK'):
        print('LIST:')
        for l in pkt['list']:
            print(l)


def get(filename, name_to_save):
    data = {}
    data["cmd"] = 'get'
    data['filename'] = 'b.txt'
    msg = json.dumps(data)
    pkt_str = kirim_data(msg)
    pkt = json.loads(pkt_str)
    print('---------------')
    print(f"RESPONS: {pkt['res']}")
    if(pkt['res']=='OK'):
        print(f'saving file to {name_to_save}')
        raw_content = b64decode(pkt['content'])
        f = open(name_to_save, 'wb')
        f.write(raw_content)
        f.close()
        print(f'file successfully saved to {name_to_save}')


def put(src, dst):
    data={}
    data["cmd"] = 'put'
    data['filename'] = dst
    f = open(src, 'rb')
    raw_content = f.read()
    f.close()
    content = b64encode(raw_content)
    data['content'] = content.decode()
    msg = json.dumps(data)
    pkt_str = kirim_data(msg)
    pkt = json.loads(pkt_str)
    print('---------------')
    print(f"RESPONS: {pkt['res']}")
    

def kirim_data(msg):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('localhost', 10000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        logging.warning(f"[CLIENT] sending {msg}")
        sock.sendall(msg.encode())
        sock.shutdown(socket.SHUT_WR)
        
        # Look for the response
        pkt = ''
        while True:
            data = sock.recv(16)
            if data:
                pkt+=data.decode()
            else:
                break        
    finally:
        logging.warning("closing")
        sock.close()
    return pkt


if __name__=='__main__':
    os.chdir('./data/client')
    put('Screenshot.jpg', 'abc.jpg')
    list()
    get('abc.jpg', 'abc.jpg')
    put('coba.txt', 'coba.txt')
