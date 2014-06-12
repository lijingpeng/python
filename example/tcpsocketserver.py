#!/usr/bin/env python
from socket import *
from datetime import datetime
import time
import sys

HOST = ''
PORT = 6666
BUFSIZE = 1024
ADDR = (HOST, PORT)

# TCP server
try:
    tcpSerSoc = socket()
    tcpSerSoc.bind(ADDR)
    tcpSerSoc.listen(5)
except socket.error, msg:
    print 'Socket Error! Create, bind, listen' + str(msg[0] + ', Error message:' + msg[1])
    sys.exit()
except Exception, errcode:
    if errcode[0] == 10035:
        print 'Error Code:10035'
    if errcode[0] == 'timed out':
        print 'Time out'

while 1:
    print 'Waiting for connection...'
    tcpCliSoc, addr = tcpSerSoc.accept()
    print addr, ' connected to server'

    while 1:
        try:
            data = tcpCliSoc.recv( BUFSIZE )
        except socket.error, msg:
            print 'Socket Error! Recv' + str(msg[0] + ', Error message:' + msg[1])
            sys.exit()
        except Exception, errcode:
            if errcode[0] == 10035:
                print 'Error Code:10035'
            if errcode[0] == 'timed out':
                print 'Time out'

        if not data: break
        print datetime.now(), "\n", data
        # time.sleep(1)
        try:
            tcpCliSoc.send("Welcome to the server, message:\n[" + data + "]\nReceived successfully!")
        except socket.error, msg:
            print 'Socket Error! send' + str(msg[0] + ', Error message:' + msg[1])
            sys.exit()
        except Exception, errcode:
            if errcode[0] == 10035:
                print 'Error Code:10035'
            if errcode[0] == 'timed out':
                print 'Time out'

    tcpCliSoc.close()
    print addr, ' close the connection.'
tcpSerSoc.close()
