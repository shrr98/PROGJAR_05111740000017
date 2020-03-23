from directory import Directory
import json
import base64

'''
PROTOCOL FORMAT

setiap paket request memiliki format json dan selalu memuat key "cmd" 
yang merupakan command request


FITUR:

- list : melihat daftar file
  command   : list
  parameter : none
  response  : { 'res' : 'OK', 'list' : daftar file }

- put : meletakkan file
  command   : put
  parameter : filename, content
  response  : berhasil          -> { 'res' : 'OK'}
              gagal (duplicate) -> { 'res' : 'ERRDUP' }

- get : mengambil file
  command   : get
  parameter : filename
  response  : berhasil          -> { 'res' : 'OK', 'content' : isi file }
              gagal (Not Found) -> { 'res' : 'ERRNF', 'content' : None }

- jika command tidak dikenali
  response  : { 'res' : 'ERRCMD' }

'''

class Protocol:
    def __init__(self):
        self.directory = Directory()
    
    def proses(self, json_to_process):
        obj = json.loads(json_to_process)
        pkt = {}
        try:
            command = obj['cmd']
            if command == 'list':
                pkt['list'] = self.directory.get_list()
                res = 'OK'
            elif command == 'get':
                filename = obj['filename']
                ret, binary = self.directory.get_file(filename)
                content = binary.decode()
                pkt['content'] = content
                res = 'OK' if ret else 'ERRNF'
            elif command == 'put':
                filename = obj['filename']
                raw_content = obj['content']
                content = raw_content.encode()
                ret = self.directory.put_file(filename, content)
                res = 'OK' if ret else 'ERRDUP'
            else:
                res = 'ERRCMD'
        except:
            res = 'ERROR'
        finally:
            pkt['res'] = res
            return json.dumps(pkt)


if __name__=='__main__':
    p = Protocol()

    # prepare packet

    f = open('abc.txt', 'rb')
    lines = f.read()
    f.close()
    data = {}
    data['cmd'] = 'get'
    data['filename'] = 'b.txt'
    hasil = p.proses(json.dumps(data))
    print(hasil)
