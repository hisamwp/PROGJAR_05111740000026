import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 30001)
print("connecting to {}".format(server_address))
sock.connect(server_address)

file_name=sys.argv[1]
buf=1024

try:
    #mengirim nama file
    sock.sendto(file_name.encode(),server_address)
    #membuka file dan membaca
    data = sock.recv(buf)
    print('Receive file...')
    while(data):
        file = open('received_' + file_name, 'wb')
        file.write(data)
        sock.settimeout(2)
        data =sock.recv(buf)
    print("File received.")
except:
    file.close()
    sock.close()
