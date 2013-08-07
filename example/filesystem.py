#!/usr/bin/env python
# operation of file system
import os

# get current dir
currDir = os.getcwd()
print 'current dir:', currDir

# list dir
print 'current dir contains:', os.listdir(currDir)

# test if it is a dir
for dirname in ('/home', 'C:/windows'):
	if os.path.isdir( dirname ):	# Test dir
		print dirname, 'is a foulder'
	else:
		dirname = ''

dirname = '/home/lijingpeng'
if dirname:
	os.chdir(dirname)		# Enter in this dir
	cwd = os.getcwd()
	print 'current dir:', cwd
	print 'current dir contains:', os.listdir(cwd)

fp = open('test', 'w')
fp.write('1\n')
fp.write('2\n')
fp.close()
print 'After create new file:', os.listdir(dirname)

# rename file name
os.rename('test', 'test.txt')
print 'After create new file:', os.listdir(dirname)

# Create full path name
path = os.path.join(dirname, os.listdir(dirname)[0])
print path

# Split the path
print os.path.split(path)
