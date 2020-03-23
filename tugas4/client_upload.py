import sys
import socket
import os
import base64

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8889)
print(f"connecting to {server_address}")
sock.connect(server_address)

file = input("Masukkan nama file: ")
command = "upload "+ file
#buka file untuk dibaca isinya
f = open("Client/" + file, "rb")
isifile = base64.encodestring(f.read())
f.close()
#melakukan encoding pada isi file
f = open("base64encode","wb")
f.write(isifile)
f.close()
#membaca hasil encoding file
f = open("base64encode","rb")
l = command.encode()+(b" ")+f.read(1024)

print("uploading file...")
while (l):
    sock.send(l)
    l =f.read(1024)
    data = sock.recv(1024)
print("file uploaded.")

print("closing connection...")
sock.close()