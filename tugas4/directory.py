import subprocess
import os
from base64 import b64encode, b64decode

class Directory:
    def __init__(self, dir='./data/server'):
        self.root = dir

    def get_list(self):
        raw_list = subprocess.getoutput('ls ' + self.root)
        list = raw_list.split('\n')
        return list
    
    def get_file(self, filename)-> (bool, str):
        path = os.path.join(self.root, filename)
        if os.path.exists(path):
            f = open(path, 'rb')
            raw_content = f.read()
            f.close()
            content = b64encode(content)
            return (True, content)
        else:
            return (False, None)

    def put_file(self, filename, content) -> bool:
        path = os.path.join(self.root, filename)
        if os.path.exists(path):
            return False
        raw_content = b64decode(content)
        f = open(path, 'wb')
        f.write(raw_content)
        f.close()
        return True

if __name__ == '__main__':
    d = Directory()
    print( f'List: {d.get_list()}' )

    # put file
    f = open('abc.txt', 'r')
    raw_content = f.read()
    content = b64encode(raw_content)
    if d.put_file('abc.txt', content):
        print('successfully put file in root dir')
    else:
        print('File already exist in root dir')

    print( f'List: {d.get_list()}' )

    # get file
    ret, content = d.get_file('abc.txt')
    if ret:
        raw_content = b64decode(content)
        f = open('def.txt', 'w')
        f.write(raw_content)
        f.close()
        print('File found and successfully save to def.txt')
    else:
        print('File doesnt exist in root dir')
