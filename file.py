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
		print sLine
	else:
		done = 1
# close all the file operater
fread.close();
# fwrite.close();
# frw.close();
# frb.close();
