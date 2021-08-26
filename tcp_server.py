import socket

host = '127.0.0.1'
port_num = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((host, port_num))

sock.listen(1)

conn,addr = sock.accept()
print('Bağlantı adresi', addr)

data = conn.recv(1024)
print("Alınan data:", data.decode())

conn.send(data) 
conn.close()

