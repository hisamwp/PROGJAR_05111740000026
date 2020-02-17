import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('127.0.0.1', 30001)
print("starting up on {}".format(server_address))
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
#buffer
buf=1024
while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print("connection from {}".format(client_address))
    # Receive the data in byte
    while True:
        #menerima nama file
        file_name = connection.recv(buf)
        #print(f"received {data}")
        #membuat directory file baru (setelah diterima server)
        dir = file_name.decode()
        dirf = 'download_' + dir
        print ("Received File:" + file_name.decode())
        f = open(dirf,'wb')
        #menerima isi file dari client
        data = connection.recv(buf)
        #print(data.decode())
        #menulis isi file
        try:
            while(data):
                f.write(data)
                sock.settimeout(2)
                data = sock.recv(buf)
        except:
            f.close()
            print ("File Downloaded")
            break;
    # Clean up the connection
    connection.close()
    break
sock.close()