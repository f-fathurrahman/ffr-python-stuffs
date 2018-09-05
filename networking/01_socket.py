import socket
import sys

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
except socket.error as err:
    print("Failed to create socket")
    print("Reason: %s" % str(err))
    
print("Socket is created successfully!")

target_host = input("Enter the target host name to connect: ")
target_port = input("Enter the target port: ")

try:
    sock.connect( (target_host, int(target_port)) )
    print("Socket is connected to %s on port %s" % (target_host, target_port))
    sock.shutdown(2)
#
except socket.error as err:
    print("Failed to connect to %s on port %s" % (target_host, target_port))
    print("Reason: %s" % str(err))
    sys.exit()

