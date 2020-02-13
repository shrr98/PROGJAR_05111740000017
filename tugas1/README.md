# Tugas 1 : Basic Socket Programming

## Tugas 1 a
### Client
Client mentransfer FILE bernama __FILES/tobesent.jpg__ ke server melalui socket.

### Server
Server menerima FILE dari client berupa chunks dan menyimpannya dengan path __FILES/receivedbyserver.jpg__.

[ ISSUE ]
```python
data = connection.recv(CHUNK_SIZE)
if data:
    # some codes
else:
    break
```
Dengan code di atas, server tidak pernah masuk ke blok **else**. Begitu juga dengan snippet code di bawah ini:
```python
data = connection.recv(CHUNK_SIZE)
if len(data) > 0:
    # some codes
else:
    break
```
Ini dikarenakan server masih menunggu untuk menerima message selanjutnya. Padahal, client telah selesai mengirim semua chunks.
Sehingga, dilakukan modifikasi pada code menjadi:
```python
data = connection.recv(CHUNK_SIZE)
# some codes
if len(data) < CHUNK_SIZE:
    break
```

## Tugas 1 b
### Client
Client mengirimkan request nama file kepada server, kemudian menunggu server mengirimkan FILE yang di-request.

### Server
Server menerima request dari client berupa nama file, kemudian mengirimkan file tersebut kepada client berupa chunks.