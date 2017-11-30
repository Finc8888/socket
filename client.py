from socket import *
import sys

server_host = '34.206.101.184'
server_port = 80

mes = [b'Hello server!']

if len(sys.argv) > 1:
	server_host = sys.argv[1]
	if len(sys.argv) > 2:
		mes = (x.encode() for x in sys.argv[2:])

s = socket(AF_INET, SOCK_STREAM)

try:
	s.connect((server_host, server_port))
	print('Connect complite')
except error as msg:
        print('Connect failed. Error Code : ', msg)
        sys.exit()

for line in mes:
	s.send(line)
	data = s.recv(1024)
	print('Client received:', data)
s.close()


