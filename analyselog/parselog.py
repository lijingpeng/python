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
#fwrite.write("line sb win opokers actions oactions\n")
dataOutput = ""

# open files and parse it
fileCount = 0
for logfile in logFiles:
    fileCount += 1
    print "Parsing file ", fileCount
    fread = open( LogFolder + logfile )
    lineCount = 0
    dataLine = fread.readline()
    while dataLine and lineCount < 3000:
        if dataLine[0] != "#":
            lineCount += 1
            dataOutput += str(lineCount) + "#"
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
            # store the champion, small blind or big blind
            dataOutput += str(championIndex) + "#"

            # if the champion is the winner
            if championIndex == winnerIndex:
                dataOutput += "1"
            else:
                dataOutput += "0"
            #print "winner ", winnerIndex

            # get all the pokers into pokers
            pokers_a = dataPiece[3].split("|")
            strTmp = pokers_a[1]
            pokers_b = strTmp.split("/")
            pokers = [pokers_a[0]] + pokers_b
            dataOutput += "#" + pokers[championIndex]
            for i in range(2, len(pokers), 1):
                dataOutput += "|" + pokers[i]

            # get actions
            dataOutput += "#" + dataPiece[2] + "#"
            actions = dataPiece[2].split("/")

            # opponent's action sequence
            oppoActions = ""
            chmpActions = ""
            listTmp = list(actions[0])
            # the champion is the small blind, he goes first
            for i in range(championIndex,len(listTmp), 2):
                oppoActions += listTmp[i]
                if i - 1 >= 0:
                    chmpActions += listTmp[i - 1]
            pass

            # after pre-flop, the action sequence is changed
            for i in range(1 , len(actions), 1):
                oppoActions += "|"
                chmpActions += "|"
                listTmp = list(actions[i])
                listOpIndex = []
                listOpIndexTmp = []
                for i in range(len(listTmp)):
                    listOpIndex += [i]
                # the champion is the small blind, he goes first
                if championIndex == 1:
                    for i in range(0,len(listTmp), 2):
                        oppoActions += listTmp[i]
                        listOpIndexTmp += [i]
                    pass
                    for i in listOpIndexTmp:
                        listOpIndex.remove(i)
                    pass
                    for i in listOpIndex:
                        chmpActions += listTmp[ i ]
                    pass

                else:
                    for i in range(1,len(listTmp), 2):
                        oppoActions += listTmp[i]
                        listOpIndexTmp += [i]
                    pass
                    for i in listOpIndexTmp:
                        listOpIndex.remove(i)
                    pass
                    for i in listOpIndex:
                        chmpActions += listTmp[ i ]
                    pass

            # Store all the opponent's actions
            dataOutput += oppoActions
            dataOutput += "#" + chmpActions
            dataOutput += "\n"
            fwrite.write(dataOutput)
            dataOutput = ""

        dataLine = fread.readline()

print len(logFiles) * 3000
print "Done."