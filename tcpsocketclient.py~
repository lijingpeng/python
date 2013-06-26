#!/usr/bin/env python

import socket

HOST = 'localhost'
PORT = 6666
BUFSIZE = 1024
ADDR = (HOST, PORT)

# TCP socket
try:
    tcpCliSoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    tcpCliSoc.connect(ADDR)
except socket.error, msg:
    print 'Socket Error! Create, bind, listen' + str(msg[0] + ', Error message:' + msg[1])
    sys.exit()
except Exception, errcode:
    if errcode[0] == 10035:
        print 'Error Code:10035'
    if errcode[0] == 'timed out':
        print 'Time out'

while 1:
    data = raw_input('>')
    if not data: break
    if data == 'exit': 
        break
        print 'Client close the connection'
    
    try:        
	tcpCliSoc.send(data)
    except socket.error, msg:
        print 'Socket Error! Create, bind, listen' + str(msg[0] + ', Error message:' + msg[1])
        sys.exit()
    except Exception, errcode:
        if errcode[0] == 10035:
            print 'Error Code:10035'
        if errcode[0] == 'timed out':
            print 'Time out'

    try:
        data = tcpCliSoc.recv(BUFSIZE)
    except socket.error, msg:
        print 'Socket Error! Create, bind, listen' + str(msg[0] + ', Error message:' + msg[1])
        sys.exit()
    except Exception, errcode:
        if errcode[0] == 10035:
            print 'Error Code:10035'
        if errcode[0] == 'timed out':
            print 'Time out'

    if not data: break
    print data

tcpCliSoc.close()
