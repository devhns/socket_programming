import socket

host = '127.0.0.1'
port_num = 5000
mesaj= "Merhaba :)!"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port_num))

sock.send(mesaj.encode())

data = sock.recv(1024)
sock.close()

print("Alınan data:", data.decode())


