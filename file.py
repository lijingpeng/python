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
