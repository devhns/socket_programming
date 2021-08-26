import socket

host = "127.0.0.1"
port_num = 5005

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.bind((host, port_num))

while True:
    data,addr = sock.recvfrom(1024)
    print ("Mesaj teslim alındı.")
    print ("Mesajın yeni hali:",data.decode())


