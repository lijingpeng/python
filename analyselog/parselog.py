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

fwrite = open(OutputFile, "w")
dataOutput = ""
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

            # Find the winner index
            winner = dataPiece[4].split("|")
            winnerIndex = 0
            if string.atoi( winner[1] ) > 0:
                winnerIndex = 1 # small blind win
            else:
                winnerIndex = 0 # big blind win

            # find the champion index
            championIndex = 0
            championName = dataPiece[5].split("|")
            if championName[0] == Champion:
                championIndex = 0
            else:
                championIndex = 1

            # if the champion is the winner
            if championIndex == winnerIndex:
                dataOutput += "1"
            print "winner ", winnerIndex

            # get all the pokers into pokers
            pokers_a = dataPiece[3].split("|")
            strTmp = pokers_a[1]
            pokers_b = strTmp.split("/")
            pokers = [pokers_a[0]] + pokers_b
            dataOutput += "#" + pokers[championIndex]
            for i in range(2, len(pokers), 1):
                dataOutput += "|" + pokers[i]
            #print dataPiece[2] # action
            #print dataPiece[3] # poker
            #print dataPiece[4] # pot
            #print dataPiece[5] # opponent

            dataOutput += "\n"
            fwrite.write(dataOutput)
            dataOutput = ""

        dataLine = fread.readline()

print len(logFiles) * 3000
print "Done."