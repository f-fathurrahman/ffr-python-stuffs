import zmq

context = zmq.Context()

# Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5678")

socket.send("Please load request")

# Get the reply
message = socket.recv()
print("I received reply [%s]" % message)
