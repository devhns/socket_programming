import socket
import time

host = "127.0.0.1"
port_num = 5005

while True:
	text = input('Bir kelime ya da cumle giriniz:')
	message = text.encode()

	print ("UDP IP adresi", host)
	print ("UDP port numarası:", port_num)
	print ("Mesajınız:", message.decode())

	sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	
	sock.sendto(message.upper(),(host,port_num))
	
	time.sleep(60)

