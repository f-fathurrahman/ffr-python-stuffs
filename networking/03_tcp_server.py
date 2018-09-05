import socket
from time import ctime

HOST = "0.0.0.0" #"localhost"
PORT = 12345
BUFSIZE = 1024
ADDR = (HOST,PORT)

server_sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
server_sock.bind(ADDR)

server_sock.listen(5)

server_sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )


try:

    while True:
        print("Server waiting for connection ...")

        client_sock, addr = server_sock.accept()
        print("Client connected from: ", addr)

        while True:
            data = client_sock.recv(BUFSIZE)
            if not data or data.decode("utf-8") == "END":
                print("No data or receiving \"END\"")
                print("I will not do nothing")
                break

            print("Received from client: %s" % data.decode("utf-8"))
        
            timenow = ctime()
            print("Sending server time to client")     
            client_sock.send( bytes(timenow,"utf-8") )

        client_sock.close()
        #
except KeyboardInterrupt:
    print()
    print("----------------------------------")
    print("Server is shutdown by user request")
    print("----------------------------------")

server_sock.close()



