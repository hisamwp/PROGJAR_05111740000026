import shelve
import uuid
import json
import os
import base64

class File:
    def upload(self,nama=None, isi=None):
        if (nama is None):
            return False

        data_file = isi
        f = open("Server/"+nama,"wb")
        f.write(base64.decodestring(data_file))
        return True
    def download(self,nama=None):
        # read file
        l = ''
        with open("Server/"+nama, "rb") as imageFile:
            str = base64.b64encode(imageFile.read())
            # print(str)
            l=l+str.decode()
            # print(l[0])
        return l;
    def list(self):
        list = os.listdir("Server")
        f = []
        for filename in list:
            f.append(filename)
        return f

if __name__=='__main__':
    p = File()
    print(p.download("jerry.jpg"))