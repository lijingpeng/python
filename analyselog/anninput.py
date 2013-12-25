__author__ = 'lijingpeng'

# Generate ann input


# Global data
dataFile = "/home/lijingpeng/Public/annout.txt"
annDataFile = "/home/lijingpeng/Public/ann.txt"


def GetRaiseCount(op_actions):
    count = 0
    for i in op_actions:
        if i == "r":
            count += 1
    pass

    return count

def GetRaiseCountStage(actions, index, op_index):
    count = 0
    startIndex = 0
    if op_index == 0:
        startIndex = 0
    else:
        startIndex = 1
    for i in range(startIndex, index, 2):
        if actions[i] == "r":
            count += 1
    pass

    return count

# get current stage money
# @actions : current action in specific stage
# @round : specify pre-flop or not
# return : [sbTotal, bbTotal]
def GetStageMoney(actions, round):
    global sbTotal
    global bbTotal
    sbTotal = 0
    bbTotal = 0
    raiseUnit = 10
    if round > 1:
        raiseUnit = 20
    else:
        raiseUnit = 10
    pass

    if round == 0:  # pre-flop round, small blind goes first
        sbTotal = 5
        bbTotal = 10
        for i in range(len(actions)):
            # 0, 2, 4 for small blind
            # 1, 3 for big blind
            if actions[i] == "c": # call
                if i % 2 == 0: # sb
                    sbTotal += abs(bbTotal - sbTotal)
                else:   # bb
                    bbTotal += abs(bbTotal - sbTotal)
                pass
            elif actions[i] == "r":
                if i % 2 == 0: # sb
                    sbTotal += abs(bbTotal - sbTotal) + raiseUnit
                else:   # bb
                    bbTotal += abs(bbTotal - sbTotal) + raiseUnit
            else:
                pass
            pass
        pass
    else: # after pre-flop stage: big blind goes first
        sbTotal = 0
        bbTotal = 0
        for i in range(len(actions)):
            # 0, 2, 4 for big blind
            # 1, 3 for small blind
            if actions[i] == "c":
                if i % 2 == 0: # bb
                    bbTotal += abs(bbTotal - sbTotal)
                else:           # sb
                    sbTotal += abs(bbTotal - sbTotal)
                pass
            elif actions[i] == "r":
                if i % 2 == 0:  # bb
                    bbTotal += abs(bbTotal - sbTotal) + raiseUnit
                else:           # sb
                    sbTotal += abs(bbTotal - sbTotal) + raiseUnit
                pass
            else:
                pass
        pass
    pass

    retVal = []
    retVal += [ sbTotal ]
    retVal += [ bbTotal ]
    return retVal

########## main process here ###########
# open output file
fileWriter = open(annDataFile, "w")
dataOutput = ""

# open data file and processing it
fileReader = open(dataFile)
dataLine = fileReader.readline()
lineCount = 0

while dataLine and lineCount < 10:
    #line sb win opokers actions oactions
    #1#0#0#3h8s#rf#r
    #2#1#0#AsTd|QhTs2d|2c|Jc#rc/crrc/rc/rc#c|cr|r|r
    dataLine = dataLine.strip("\n")
    dataPiece = dataLine.split("#")
    actionSet = dataPiece[4].split("/")
    if dataPiece[1] == "0" and dataPiece[5] == "f":
        dataLine = fileReader.readline()
        lineCount += 1
        continue
    print "org:", dataPiece

    index = 0
    PreFlopLen = len(actionSet[0])
    SB_TillNow = {}
    BB_TillNow = {}
    PotTillNow = {}
    OpRaiseCount = {}
    Op_CallCount = {}
    ### initialize dict
    for ac in actionSet:
        for acl in list(ac):
            if acl == "r":
                OpRaiseCount[index] = 1
                Op_CallCount[index] = 0
            elif acl == "c":
                Op_CallCount[index] = 1
                OpRaiseCount[index] = 0
            else:
                OpRaiseCount[index] = 0
                Op_CallCount[index] = 0
            pass
            PotTillNow[index] = 15
            if index == 0:
                SB_TillNow[index] = 5
                BB_TillNow[index] = 10
            else:
                SB_TillNow[index] = 0
                BB_TillNow[index] = 0
            index += 1
        pass
    pass

    for i in range(len(OpRaiseCount)):
        if i < PreFlopLen:          #######pre-flop
            if dataPiece[1] == "0": ## I am big blind, 0, 2, 4 are opponent
                if index % 2 != 0:
                    OpRaiseCount[index] = 0
                    Op_CallCount[index] = 0
                else:
                    pass
            else:                   ## I am small blind, 1, 3, 5 are opponent
                if index % 2 == 0:
                    OpRaiseCount[index] = 0
                    Op_CallCount[index] = 0
                else:
                    pass
            pass
        else:                       #######pre-flop
            if dataPiece[1] == "0": ## I am big blind, 1, 3, 5 are opponent
                if index % 2 == 0:
                    OpRaiseCount[index] = 0
                    Op_CallCount[index] = 0
                else:
                    pass
            else:                   ## I am small blind, 0, 2, 4 are opponent
                if index % 2 != 0:
                    OpRaiseCount[index] = 0
                    Op_CallCount[index] = 0
                else:
                    pass
            pass
    ### calc dict
    #for index in range(0, len(actionSet), 1):
    #    acTmp = list(actionSet[index])
    #    if index == 0: ########################################pre-flop
    #        if dataPiece[1] == "0": ###### I am big blind, 0, 2, 4 are opponent
    #            if acTmp[index] == "r" and index % 2 == 0:
    #                OpRaiseCount[index] = 1
    #            elif acTmp[index] == "c" and index % 2 == 0:
    #                Op_CallCount[index] = 1
    #            else:
    #                pass
    #        else:                   ###### I am small blind, 1, 3, 5 are opponent
    #            if acTmp[index] == "r" and index % 2 != 0:
    #                OpRaiseCount[index] = 1
    #            elif acTmp[index] == "c" and index % 2 != 0:
    #                Op_CallCount[index] = 1
    #            else:
    #                pass

    #for index in range(len(actionSequence)):
    #    if index < PosList[0]:  ############## Pre-flop stage

    #    else:               ############## after Pre-flop stage
    #        if dataPiece[1] == "0": ###### I am big blind, 0, 2, 4 are opponent
    #            if actionSequence[index] == "r" and index % 2 == 0:
    #                OpRaiseCount[index] = 1
    #            elif actionSequence[index] == "c" and index % 2 == 0:
    #                Op_CallCount[index] = 1
    #            else:
    #                pass
    #        else:                   ###### I am small blind, 1, 3, 5 are opponent
    #            if actionSequence[index] == "r" and index % 2 != 0:
    #                OpRaiseCount[index] = 1
    #            elif actionSequence[index] == "c" and index % 2 != 0:
    #                Op_CallCount[index] = 1
    #            else:
    #                pass
    #        pass
    #    pass
    #pass


    print "OpRaiseCount", OpRaiseCount
    print "Op_CallCount", Op_CallCount
    print "PotTillNow", PotTillNow
    print "SB_TillNow", SB_TillNow
    print "BB_TillNow", BB_TillNow
    print "PotTillNow", PotTillNow
    print "---------------------------------------"



    dataLine = fileReader.readline()
    lineCount += 1

print "----------------------------------------------------\nDone."