import sys
import socket
import threading

ports = [31000, 31001, 31002]

def do_thread(i):
    #server membuat socket yang akan melisten 3 port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', i)
    print(f"starting up on {server_address}")
    #bind socket dan listen
    sock.bind(server_address)
    sock.listen(1)

    while True:
        print("waiting for a connection")
        connection, client_address = sock.accept()
        #saat koneksi diterima
        print(f"Handle connection from {client_address}")
        while True:
            data = connection.recv(32)
            #menerima data
            print(f"[ Port {i}] received {data}")
            if data:
                #mengirim kembali data
                print(f"[ Port {i}] sending back data")
                connection.sendall(data)
            break

        connection.close()

# Listen untuk koneksi yang akan datang
multi_threads = []
for i in ports:    
    thr = threading.Thread(target=do_thread, args=(i,))
    multi_threads.append(thr)

for thr in multi_threads:
    thr.start()

print('Exit')