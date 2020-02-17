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
        print ("Requested file:" + file_name.decode())
        f = open(file_name.decode(),'rb')
        #membaca isi file yang direquest client
        data = f.read();
        connection.sendto(data, client_address)
        while (data):
            #mengirim ke client
            if(connection.sendto(data,server_address)):
                print ("sending ...")
                data = f.read(buf)
        print('File sent')
        break
    # Clean up the connection
    connection.close()
    break
sock.close()