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
    #line sb win opokers actions oactions
    #1#0#0#3h8s#rf#r
    #2#1#0#AsTd|QhTs2d|2c|Jc#rc/crrc/rc/rc#c|cr|r|r
    #3#0#1#QsJs#f#f
    #4#1#1#JsQs|6dQd9h#rc/crf#c|cf
    #5#0#0#TdKs|Jd4c8s|Ac|2c#rc/crc/cc/crc#r|r|c|r
    #6#1#0#Kd4s|Kc6sAd|Ac|9h#rrc/rc/rc/rc#r|r|r|r
    #7#0#0#Qd7c|4h9s8s|4s#rc/cc/crf#r|c|r
    #8#1#0#Th2h|Ad4d3d|8d#rc/crrc/rf#c|cr|r
    #9#0#0#QhJd|5hAs6c|Tc|Th#rc/crc/crc/crc#r|r|r|r
    print dataLine
    dataLine = fileReader.readline()
    lineCount += 1
    pass

print "----------------------------------------------------\nDone."