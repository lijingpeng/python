__author__ = 'lijingpeng'

dataFile = "/home/lijingpeng/Public/test.csv"
trainFile ="/home/lijingpeng/Public/strain.csv"
testFile = "/home/lijingpeng/Public/stest.csv"

fileWriterTrain = open(trainFile, "w")
fileWriterTest = open(testFile, "w")
fileReader = open(dataFile)
lineCount = 0
dataLine = fileReader.readline()
while dataLine:
    lineCount += 1
    print lineCount
    if lineCount < 37458:
        fileWriterTest.write(dataLine)
    else:
        fileWriterTrain.write(dataLine)
    dataLine = fileReader.readline()
pass

fileReader.close()
fileWriterTest.close()
fileWriterTrain.close()
print "++++++++++++++++++++++++++++++++"
print "Done."