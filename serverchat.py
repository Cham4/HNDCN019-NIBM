import socket
import sys

def socket_create():
	try:
		global host
		global port
		global s
		host='127.0.0.1'
		port=65000
		s=socket.socket()
	except socket.error as msg:
		print('creation error' + str(msg))
def socket_bind():
	try:
		global host
		global port
		global s
		print('binding socket to port' + str(port))
		s.bind((host,port))
		s.listen(5)
	except socket.error as msg:
		print('binding error '+str(msg +'\n'+'retrying_:'))
		socket_bind()
def socket_accept():
	conn, address=s.accept()
	print('connection established: '+'ip address '+address[0])
	send_commands(conn)
	conn.close()
def send_commands(conn):
	while True:
		cmd=input()
		if cmd=='Q':
			conn.close()
			sys.exit()
		if len(str.encode(cmd)) > 0:
			response=str(conn.recv(1024), 'utf-8')
			print(response, end='')
def main():
	socket_create()
	socket_bind()
	socket_accept()
main()
