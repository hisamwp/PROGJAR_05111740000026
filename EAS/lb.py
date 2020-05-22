import socket
import time
import sys
import asyncore
import logging
import os
import threading

class BackendList:
	def __init__(self):
		self.servers=[]
		self.servers.append(('127.0.0.1',9002))
		self.servers.append(('127.0.0.1',9003))
		self.servers.append(('127.0.0.1',9004))
		self.most_port = 9004
		self.most_treshold = 100
		self.client_num = 0
		self.current=0
	def getserver(self,client_num):
		s = self.servers[self.current]
		self.current=self.current+1
		if (self.current>=len(self.servers)):
			self.current=0
		self.client_num = client_num
		return s
	def checkConnection(self):
		if self.client_num > self.most_treshold:
			logging.warning("starting server")
			cmd = """ python3 async_server.py %d &""" % (self.most_port+1)
			logging.warning(cmd)
			res = os.system(cmd)
			if res:
				logging.warning("failed to start new server at {}" . format(self.most_port+1))
				return
			time.sleep(.5)
			logging.warning("new server is starting at port {}" . format(self.most_port))
			self.addNewServer(self.most_port+1,self.most_treshold+50)
			# x = threading.Thread(target=start_new_server, args=(self.most_port,self.most_treshold,self))
			# x.start()
	def addNewServer(self,new_port, new_treshold):
		self.servers.append(('127.0.0.1',new_port))
		self.most_port = new_port
		self.most_treshold = new_treshold



class Backend(asyncore.dispatcher_with_send):
	def __init__(self,targetaddress):
		asyncore.dispatcher_with_send.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connect(targetaddress)
		self.connection = self

	def handle_read(self):
		try:
			self.client_socket.send(self.recv(8192))
		except:
			pass
	def handle_close(self):
		try:
			self.close()
			self.client_socket.close()
		except:
			pass

class ThreadCheck(threading.Thread):
	def __init__(self,bserver):
		self.bservers = bserver
		threading.Thread.__init__(self)
	
	def run(self):
		while 1:
			time.sleep(.1)
			# print('thread dijalankan')
			self.bservers.checkConnection()


class ProcessTheClient(asyncore.dispatcher):
	def handle_read(self):
		data = self.recv(8192)
		if data:
			self.backend.client_socket = self
			self.backend.send(data)
	def handle_close(self):
		self.close()

class Server(asyncore.dispatcher):
	def __init__(self,portnumber):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.set_reuse_addr()
		self.bind(('',portnumber))
		self.listen(5)
		self.bservers = BackendList()
		self.timer = ThreadCheck(self.bservers)
		self.timer.start()
		# logging.warning("load balancer running on port {}" . format(portnumber))

	def handle_accept(self):
		pair = self.accept()
		if pair is not None:
			sock, addr = pair
			# logging.warning("connection from {}" . format(repr(addr)))

			#menentukan ke server mana request akan diteruskan
			bs = self.bservers.getserver(len(asyncore.socket_map))
			logging.warning("koneksi dari {} diteruskan ke {}" . format(addr, bs))
			backend = Backend(bs)

			#mendapatkan handler dan socket dari client
			handler = ProcessTheClient(sock)
			handler.backend = backend

# def start_new_server(port,treshold,bservers):
# 	cmd = """ python3 async_server.py %d &""" % (port+1)
# 	# logging.warning(cmd)
# 	res = os.system(cmd)
# 	if res:
# 		logging.warning("failed to start new server at {}" . format(port+1))
# 		return
# 	bservers.addNewServer(port+1,treshold+50)
	# logging.warning("new server is starting at port {}" . format(self.most_port))



def main():
	portnumber=44444
	try:
		portnumber=int(sys.argv[1])
	except:
		pass
	svr = Server(portnumber)
	asyncore.loop()

if __name__=="__main__":
	main()


