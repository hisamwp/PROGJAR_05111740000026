import sys
import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8889)
print(f"connecting to {server_address}")
sock.connect(server_address)

command ="list"
datasend = command.encode()
print(f"getting {command}...")
sock.send(datasend)
sock.shutdown(socket.SHUT_WR)
hasil = sock.recv(1024).decode()
print(hasil)

print("closing connection...")
sock.close()