#!/usr/bin/env python
from datetime import *
import time
from time import ctime

print 'data.max',date.max
print 'date.min',date.min

# Today
now = date.today()
print 'Today:', now
print 'Datetuple', now.timetuple()
print 'Isocalendar', now.isocalendar()
print 'Isoformat', now.isoformat()

print '-------------------------------------------------------------------'
print 'datetime.max:', datetime.max 
print 'datetime.min:', datetime.min 
print 'datetime.resolution:', datetime.resolution 
print 'today():', datetime.today() 
print 'now():', datetime.now() 
print 'utcnow():', datetime.utcnow() 
print 'fromtimestamp(tmstmp):', datetime.fromtimestamp(time.time()) 
print 'utcfromtimestamp(tmstmp):', datetime.utcfromtimestamp(time.time()) 

print 'ctime(time()) Current time is:', time.ctime(time.time())
