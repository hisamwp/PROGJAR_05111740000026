import sys
import socket
import os
import base64

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8889)
print(f"connecting to {server_address}")
sock.connect(server_address)

nama = input("Masukkan file yang ingin di download: ")
request = (b"download "+nama.encode())
print("Mendownload file "+request.decode()+"...")
f = open("Client/"+nama,"wb")
file =(b"")
sock.send(request)
data = sock.recv(1024)
print(data)

file = base64.b64decode(data)
f.write(file)
f.close()

print("file "+nama+" berhasil didownload")
sock.close()