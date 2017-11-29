from socket import *
import sys

my_host = ''
my_port = 10000

s = socket(AF_INET, SOCK_STREAM)
try:
	s.bind((my_host, my_port))
	print('Binding complite')
except error as msg:
        print('Bind failed. Error Code : ', msg)
        sys.exit()
 
try:
	s.listen(5)
	print('Server redy to listen...')
except:
	print('Server dont redy to listen')

while True:
	try:
		conn, adress = s.accept()
		print('Connecting by', adress[0], ':', adress[1])
	except:
		print('Connecting dont accept')
	while True:
		try:
			data = conn.recv(1024)
			if not data: break
			print('Recive data:',data)
		except:
			print('Error recive')
		try:
			conn.send(b'Echo -->' + data)
			print('Data send')
		except:
			print('Error send')
	conn.close()
