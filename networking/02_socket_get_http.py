import socket

HOST = "tf.itb.ac.id"
PORT = 80 #443=https 80 = http
BUFSIZE = 4096
ADDR = (HOST,PORT)

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(ADDR)

while True:
    data = "GET / HTTP/1.0\n\n"
    if not data:
        break
    client_sock.send(data.encode("utf-8"))
    data = client_sock.recv(BUFSIZE)
    if not data:
        break
    print(data.decode("utf-8"))

client_sock.close()


