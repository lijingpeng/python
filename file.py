# python file operation

# 1. open file
fread = open('/home/lijingpeng/test.txt')
fwrite = open('/home/lijingpeng/test.txt', 'w')
frw = open('/home/lijingpeng/test.txt', 'r+')
frb = open('/home/lijingpeng/test.txt', 'rb')

# close all the file operater
fread.close();
fwrite.close();
frw.close();
frb.close();
