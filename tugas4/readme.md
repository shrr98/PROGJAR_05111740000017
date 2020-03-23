# CUSTOM FILE TRANSFER PROTOCOL

## PROTOCOL FORMAT
setiap paket request memiliki format json dan selalu memuat key "cmd" 
yang merupakan command request


FITUR:

- list : melihat daftar file<br/>
  command   : list<br/>
  parameter : none<br/>
  response  : { 'res' : 'OK', 'list' : daftar file }<br/>

- put : meletakkan file<br/>
  command   : put<br/>
  parameter : filename, content<br/>
  response  : berhasil          -> { 'res' : 'OK'}<br/>
              gagal (duplicate) -> { 'res' : 'ERRDUP' }<br/>

- get : mengambil file<br/>
  command   : get<br/>
  parameter : filename<br/>
  response  : berhasil          -> { 'res' : 'OK', 'content' : isi file }<br/>
              gagal (Not Found) -> { 'res' : 'ERRNF', 'content' : None }<br/>

- jika command tidak dikenali<br/>
  response  : { 'res' : 'ERRCMD' }<br/>

## CLIENT
- List
- Get
- Put