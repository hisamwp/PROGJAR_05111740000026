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
    file=open(file_name,"rb")
    data = file.read(buf)
    #print(data.decode())
    #mengirim isi file dalam byte
    sock.sendto(data,server_address)
    while (data):
        if(sock.sendto(data,server_address)):
            print ("sending ...")
            data = file.read(buf)  
finally:
    print("closing")
    sock.close()
    file.close()
