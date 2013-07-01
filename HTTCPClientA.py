#!/usr/bin/env python

import socket
import binascii
import time

HOST = '219.223.252.170'
PORT = 6010
BUFSIZE = 307
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

data = binascii.a2b_hex("53553700074313062717121000180023004400000000000000000000000000000000480030AA000300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004C000080BF000080BF0000000000002041303030303030000212313233343536373839303132303030456B6F")
sendCount = 0;
while 1:
    sendCount += 1
    print 'Send Successfully:', sendCount, ":", len(data)
    time.sleep(1)

    try:        
	tcpCliSoc.send(data)
#    re=tcpCliSoc.recv(1024)
#    print re
    except socket.error, msg:
        print 'Socket Error! Create, bind, listen' + str(msg[0] + ', Error message:' + msg[1])
        sys.exit()
    except Exception, errcode:
        if errcode[0] == 10035:
            print 'Error Code:10035'
        if errcode[0] == 'timed out':
            print 'Time out'

tcpCliSoc.close()
