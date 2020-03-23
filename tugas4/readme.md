# CUSTOM FILE TRANSFER PROTOCOL

## PROTOCOL FORMAT
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

## CLIENT
- List
- Get
- Put