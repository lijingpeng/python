#!/usr/bin/env python
import os
import random

while True:
    a = random.randint(1, 100)
    a = a % 2
    if a == 1:
        print 'Send Alert:'
        os.system('python HTTCPClientA.py')     # send alert 
    else:
        print 'Send Report'
        os.system('python HTTCPClient.py')      # send report


