import socket

HOST = "localhost" # default server name
PORT = 12345       # default server port
BUFSIZE = 1024

client_sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

host = input("Enter hostname [%s]:" % HOST) or HOST
port = input("Enter port [%s]:" % PORT) or PORT

sock_addr = (host, port)
client_sock.connect(sock_addr)

payload = "GET TIME"

try:
    while True:
        client_sock.send(payload.encode("utf-8"))
        data = client_sock.recv(BUFSIZE)
        print(repr(data))
        more = input("Do you want to send more data to server? [y/n]")
        if more.lower() == "y":
            payload = input("Enter payload: ")
        else:
            print("No more data to server, closing connection now")
            break
#
except KeyboardInterrupt:
    print("Exited by user request")

client_sock.close()

