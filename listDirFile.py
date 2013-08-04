#!/usr/bin/env python
# list file and dir in specific dir

import os
import sys

# check args
if len(sys.argv) != 2:
    print 'Command line ERROR'
    print 'Usage: listDirFile <dir>'
    sys.exit(0)
# Get target path
rootDirName = sys.argv[1]
print 'Target dir is:', sys.argv[1]

# Get all dirs
def GetAllDir(path):
    all = os.listdir(path)
    allDir = []
    for name in all:
        if os.path.isdir(os.path.join(path, name)):
            allDir.append(name)
    return allDir

# Get all files
def GetAllFiles(path):
    all = os.listdir(path)
    allfiles = []
    for name in all:
        if os.path.isfile(name):
            allfiles.append(name)
    return allfiles

# print dir and file
def PrintAll(path):
    print '\n', path
    dirs = GetAllDir(path)
    if len(dirs):
    	print ''
    else:
        for i in dirs:
            print i

    files = GetAllFiles(path)
    if len(files):
        print ''
    else:
        print ''
        for i in GetAllFiles(path):
            print i

# Get dir full path
allDir = []
def GetDirFullName(path):
    all = os.listdir(path)
    allDir.append(path)
    for name in all:
        if os.path.isdir(os.path.join(path, name)):
            allDir.append(os.path.join(path, name))
            GetDirFullName(os.path.join(path, name))
    return
#for i in GetDirFullName(rootDirName):
 #   PrintAll(i)



for parent, dirnames, filenames in os.walk(rootDirName):
    print '\n'
    for dirname in dirnames:
        #print 'Parent is:', parent
        print dirname

    for file in filenames:
        #print 'Parent is:', parent
        print os.path.join(parent, file)

