#!/usr/bin/python
# command line args

import sys

print 'Program name:', sys.argv[0]
print sys.argv[0], ' has ', len(sys.argv)-1, ' arguments.'

for i in range(1, len(sys.argv)):
    print i, sys.argv[i]
