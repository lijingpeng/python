import string

__author__ = 'lijingpeng'
# Parse log file
# input: Folder

import os, shutil

# settings
LogFolder = "/home/lijingpeng/Public/tb/"
OutputFile = "/home/lijingpeng/Public/annout.txt"
Champion = "marv"

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
            # STATE:0:rc/crc/crc/crc:Tc6d|Ks5h/QsTs2s/9s/Ah:-70|70:feste_iro|marv
            # Find the winner
            winner = dataPiece[4].split("|")
            winnerIndex = 0
            if string.atoi( winner[1] ) > 0:
                winnerIndex = 1 # small blind win
            else:
                winnerIndex = 0 # big blind win
            print "winner ", winnerIndex
            print dataPiece[2]
            print dataPiece[3]
            print dataPiece[4]
            print dataPiece[5]

        dataLine = fread.readline()

print len(logFiles) * 3000
print "Done."