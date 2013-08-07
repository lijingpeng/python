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

data = binascii.a2b_hex("534817035543130602145022002500250044339B194630303030303030303030303030303030303030303030303030303030303030303030303030303030303030309999993F303030303030303030303030303030303030303030303030303030303030303030303030303030303030303000401CC6303030303030303030303030303030303030303030303030303030303030303030303030303030303030303000401CC630303030303030303030303030303030303030303030303030303030303030303030303030303030303030300000305858585850393231392E3232332E3235322E313635373131392E3134352E382E31303700004F3436303030003531323334364C000000000080844300509A44CDCCCC3D3030303030300002353138333139343232323534303030304565F1")
sendCount = 0;
while 1:
    sendCount += 1
    print 'Send Successfully:', sendCount
    time.sleep(1)

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

tcpCliSoc.close()
