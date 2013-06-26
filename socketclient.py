#!/usr/bin/env python

import socket

HOST = 'localhost'
PORT = 6666
BUFSIZE = 1024
ADDR = (HOST, PORT)

# TCP socket
tcpCliSoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
tcpCliSoc.connect(ADDR)

while 1:
    data = raw_input('>')
    if not data: break
    if data == 'exit': 
        break
        print 'Client close the connection'
    tcpCliSoc.send(data)
    data = tcpCliSoc.recv(BUFSIZE)
    if not data: break
    print data

tcpCliSoc.close()
