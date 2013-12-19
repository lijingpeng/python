__author__ = 'lijingpeng'

# Generate ann input

# Global data
dataFile = "/home/lijingpeng/Public/annout.txt"
annDataFile = "/home/lijingpeng/Public/ann.txt"

# open data file and processing it
fileReader = open(dataFile)
dataLine = fileReader.readline()
lineCount = 0
while dataLine and lineCount < 10:
    # main process here
    print dataLine
    lineCount += 1
    pass

print "----------------------------------------------------\nDone."