from file import File
import json
import logging
import base64


'''
PROTOCOL FORMAT

string terbagi menjadi 2 bagian, dipisahkan oleh spasi
COMMAND spasi PARAMETER spasi PARAMETER ...

FITUR

- upload : untuk mengupload file
  request : upload
  parameter : namaFile spasi isiFile
  response : berhasil -> ok
             gagal -> error

- download : untuk mendownload file
  request: download
  parameter : namaFile
  response: berhasil -> hasil berupa isi file
            gagal -> ERROR

- list : untuk melihat file server
  request: list
  parameter: tidak ada
  response: daftar file yang ada di server

- jika command tidak dikenali akan merespon dengan ERRCMD

'''
f = File()

class FileMachine:
    def proses(self,string_to_process):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='upload'):
                logging.warning('upload')
                namaFile = cstring[1].strip()
                isiFile = cstring[2].strip()
                f.upload(namaFile,isiFile.encode())
                return "OK"
            elif (command=='download'):
                logging.warning("download")
                namaFile = cstring[1].strip()
                hasil = f.download(namaFile)
                return hasil
            elif (command=='list'):
                logging.warning("list")
                hasil = f.list()
                dict = {"file": hasil}
                return json.dumps(dict)
            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    fm = FileMachine()
    # hasil = fm.proses("upload coba2.txt cobalagigaes")
    # print(hasil)