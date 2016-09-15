# python file operation

filename = '/home/lijingpeng/test.txt'
# 1. open file
fread = open(filename)
# fwrite = open(filename, 'w')
# frw = open(filename, 'r+')
# frb = open(filename, 'rb')

# 2. read the file
done = 0
while not done:
	sLine = fread.readline()
	if sLine != "":
		print sLine,
	else:
		done = 1
# close all the file operater
fread.close();
# fwrite.close();
# frw.close();
# frb.close();
print '---------------Read file end-----------------'

# write file
wFilename = '/home/lijingpeng/w.txt'
fw = open(wFilename, 'w')
done = 0
while not done:
	aLine = raw_input("Enter a line:(.. to quit!)")
	if aLine != "..":
		fw.write(aLine + '\n')
	else:
		done = 1
fw.close()
 
print '---------------Write file end----------------'
fwt = open('/tmp/a', 'w+')
fwt.tell()

fwt.write('line 1\n')
fwt.tell()


fwt.write('line 2\n')
fwt.tell()

fwt.write('line 3\n')
fwt.tell()

fwt.seek(-6, 1)
fwt.tell()

fwt.readline()

fwt.seek(0, 0)

fwt.tell()

print 'File Closed', fwt.closed
print 'File Mode', fwt.mode
print 'File Name', fwt.name

fwt.close()
print '---------------Seek file end----------------'

# command line args
import sys
print 'Length of args', len(sys.argv)
print 'They are:', sys.argv

print '--------------Command line args end----------------'

