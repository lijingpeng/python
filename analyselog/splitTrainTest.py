__author__ = 'lijingpeng'

dataFile = "/home/lijingpeng/Public/strain.csv"
trainFile ="/home/lijingpeng/Public/8strain.csv"
#testFile = "/home/lijingpeng/Public/stest.csv"

fileWriterTrain = open(trainFile, "w")
#fileWriterTest = open(testFile, "w")
fileReader = open(dataFile)
lineCount = 0
dataLine = fileReader.readline()
while dataLine:
    lineCount += 1
    print lineCount
    if lineCount % 8  == 0:
        fileWriterTrain.write(dataLine)
        #fileWriterTest.write(dataLine)
    #else:
    #    fileWriterTrain.write(dataLine)
    dataLine = fileReader.readline()
pass

fileReader.close()
#fileWriterTest.close()
fileWriterTrain.close()
print "++++++++++++++++++++++++++++++++"
print "Done."