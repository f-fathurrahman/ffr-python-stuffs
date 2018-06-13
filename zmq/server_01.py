from __future__ import print_function

import time
import zmq
import random

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5678")

while True:
    # wait for next request from client
    message = socket.recv()
    print("I received request: %s" % message)
    # make everything does not happen to fast to see
    time.sleep(2)
    # send reply
    socket.send("Sending random: " + str(random.random()))


