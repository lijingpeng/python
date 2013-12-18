__author__ = 'lijingpeng'
# Parse log file
# input: Folder

import os, shutil

LogFolder = "/home/lijingpeng/Public/ta/"
# store all filename
logFiles = os.listdir( LogFolder )

# open files and parse it
fileCount = 0
for logfile in logFiles:
    fileCount += 1
    print "Parsing file ", fileCount
    fread = open( LogFolder + logfile )
    dataLine = fread.readline()
    while dataLine:
        if dataLine[0] != "#":
            # main process here
            dataPiece = dataLine.split(":")
            print dataPiece
        dataLine = fread.readline()

print len(logFiles) * 3000
print "Done."