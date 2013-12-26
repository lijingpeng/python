__author__ = 'lijingpeng'

dataFile = "/home/lijingpeng/Public/ann.txt"

fileReader = open(dataFile)
lineCount = 0
dataLine = fileReader.readline()
while dataLine and lineCount < 10:
    print dataLine

    dataLine = fileReader.readline()
    lineCount += 1