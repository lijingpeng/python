#!/usr/bin/env python
from socket import *
from time import time, ctime
from datetime import *

HOST = ''
PORT = 6666
BUFSIZE = 1024
ADDR = (HOST, PORT)

# TCP server
tcpSerSoc = socket()
tcpSerSoc.bind(ADDR)
tcpSerSoc.listen(5)

while 1:
    print 'Waiting for connection...'
    tcpCliSoc, addr = tcpSerSoc.accept()
    print addr, ' connected to server'

    while 1:
        data = tcpCliSoc.recv( BUFSIZE )
        if not data: break
        print data
        tcpCliSoc.send("Welcome to the server")
        #tcpCliSoc.send('Welcome to the server! ',time.strftime("%a %b %d %H:%M:%S", time.localtime()))
    tcpCliSoc.close()
    print addr, ' close the connection.'
tcpSerSoc.close()
