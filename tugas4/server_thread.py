from socket import *
import socket
import threading
import logging
import time
import sys
import base64


from file_machine import FileMachine

fm = FileMachine()

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        file = (b"")
        tes = []
        while True:
            while True:
              #  try:
                    data = self.connection.recv(1024)

                 #   self.connection.sendall(b"hali")
                    file = file + data
                    tes.append(data)
                    bytenya = int(sys.getsizeof(data))

                    if bytenya != 1057 :
                        break
                    else :
                        # self.connection.sendall(b"halo")
                        print("tes")
            data = file

            if data:
                d = data.decode()
                hasil = fm.proses(d)
                hasil=hasil
                print(hasil)
                self.connection.sendall(hasil.encode())
            else:
                break
        self.connection.close()


class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('localhost', 8889))
        self.my_socket.listen(1)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"connection from {self.client_address}")

            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)


def main():
    svr = Server()
    svr.start()


if __name__ == "__main__":
    main()

