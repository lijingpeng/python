__author__ = 'lijingpeng'

# Generate ann input
# Global data
dataFile = "/home/lijingpeng/Public/annout.txt"
annDataFile = "/home/lijingpeng/Public/ann.txt"
spliter = "_"

def GetRaiseCallCount(actions, opsmallorbig, stage):
    callCount = 0
    raiseCount = 0
    if opsmallorbig == 0: # op is big, 1,3 | 0 , 2
        for i in range(len(actions)):
            if stage == 0: # pre-flop, me goes first
                if i % 2 != 0:
                    if actions[i] == "r":
                        raiseCount += 1
                    elif actions[i] == "c":
                        callCount += 1
                    else:
                        pass
                pass
            else:
                if i % 2 == 0:
                    if actions[i] == "r":
                        raiseCount += 1
                    elif actions[i] == "c":
                        callCount += 1
                    else:
                        pass
                pass
            pass
        pass
    else:# op is small,  0 , 2 | 1,3
        for i in range(len(actions)):
            if stage == 0: # pre-flop, op goes first
                if i % 2 == 0:
                    if actions[i] == "r":
                        raiseCount += 1
                    elif actions[i] == "c":
                        callCount += 1
                    else:
                        pass
                pass
            else:
                if i % 2 != 0:
                    if actions[i] == "r":
                        raiseCount += 1
                    elif actions[i] == "c":
                        callCount += 1
                    else:
                        pass
                pass
            pass
        pass

    retVal = []
    retVal += [raiseCount]
    retVal += [callCount]
    return retVal


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
lineCountOut = 1

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
    print "org:", dataLine

    index = 0
    FLOP = 0
    TURN = 0
    RIVER = 0 #
    OpRaiseCount = 0
    OpCallCount = 0
    SB_TillNow = 0
    BB_TillNow = 0
    OpLastAction = ""

    ######################################################### pre-flop
    if dataPiece[1] == "1": # i am small, op big
        for i in range(len(actionSet[0])):
            if i % 2 == 0: # "me"
                actionList = list(actionSet[0][:i])
                SB_BB = GetStageMoney(actionList, 0)
                SB_TillNow = SB_BB[0]
                BB_TillNow = SB_BB[1]
                FLOP = 0
                TURN = 0
                RIVER = 0
                RA_CA = GetRaiseCallCount(actionList, 0, 0)
                OpRaiseCount = RA_CA[0]
                OpCallCount = RA_CA[1]
                if i >= 1:
                    OpLastAction = actionList[i - 1]
                dataOutput = ""
                dataOutput += str(lineCountOut) + spliter
                lineCountOut += 1
                dataOutput += dataPiece[0] + spliter
                dataOutput += dataPiece[1] + spliter
                dataOutput += dataPiece[2] + spliter
                dataOutput += str(FLOP) + spliter
                dataOutput += str(TURN) + spliter
                dataOutput += str(RIVER)+ spliter
                dataOutput += str(SB_TillNow) + spliter
                dataOutput += str(BB_TillNow) + spliter
                dataOutput += str(OpRaiseCount) + spliter
                dataOutput += str(OpCallCount) + spliter
                dataOutput += OpLastAction + "\n"
                fileWriter.write(dataOutput)
                #print dataOutput
    else:                   # i am big, op small
        for i in range(len(actionSet[0])):
            if i % 2 != 0: # "me"
                actionList = list(actionSet[0][:i])
                SB_BB = GetStageMoney(list(actionSet[0][:i]), 0)
                SB_TillNow = SB_BB[0]
                BB_TillNow = SB_BB[1]
                AllTillNow = SB_TillNow + BB_TillNow
                FLOP = 0
                TURN = 0
                RIVER = 0
                RA_CA = GetRaiseCallCount(list(actionSet[0][:i]), 1, 0)
                OpRaiseCount = RA_CA[0]
                OpCallCount = RA_CA[1]
                if i >= 1:
                    OpLastAction = actionList[i - 1]
                dataOutput = ""
                dataOutput += str(lineCountOut) + spliter
                lineCountOut += 1
                dataOutput += dataPiece[0] + spliter
                dataOutput += dataPiece[1] + spliter
                dataOutput += dataPiece[2] + spliter
                dataOutput += str(FLOP) + spliter
                dataOutput += str(TURN) + spliter
                dataOutput += str(RIVER)+ spliter
                dataOutput += str(SB_TillNow) + spliter
                dataOutput += str(BB_TillNow) + spliter
                dataOutput += str(OpRaiseCount) + spliter
                dataOutput += str(OpCallCount) + spliter
                dataOutput += OpLastAction + "\n"
                fileWriter.write(dataOutput)
                #print dataOutput
    pass
    #########################################################################
    SB_BB = GetStageMoney(actionSet[0], 0)
    SB_TillNow = SB_BB[0]
    BB_TillNow = SB_BB[1]
    AllTillNow = SB_TillNow + BB_TillNow


    if dataPiece[1] == "1": # i am small, op big 0 2
        for round in range(1, len(actionSet), 1): #####ignore pre-flop
            for i in range(len(actionSet[round])):
                if i % 2 != 0: # "me"
                    TMP_SB = 0
                    TMP_BB = 0
                    actionList = list(actionSet[round][:i])
                    SB_BB = GetStageMoney(actionList, 1)
                    TMP_SB = SB_BB[0]
                    TMP_BB = SB_BB[1]
                    if round == 1:
                        FLOP = 1
                        TURN = 0
                        RIVER = 0
                    elif round == 2:
                        FLOP = 0
                        TURN = 1
                        RIVER = 0
                    else:
                        FLOP = 0
                        TURN = 0
                        RIVER = 1
                    RA_CA = GetRaiseCallCount(actionList, 0, 1)
                    OpRaiseCount += RA_CA[0]
                    OpCallCount += RA_CA[1]
                    if i >= 1:
                        OpLastAction = actionList[i - 1]
                    dataOutput = ""
                    dataOutput += str(lineCountOut) + spliter
                    lineCountOut += 1
                    dataOutput += dataPiece[0] + spliter
                    dataOutput += dataPiece[1] + spliter
                    dataOutput += dataPiece[2] + spliter
                    dataOutput += str(FLOP) + spliter
                    dataOutput += str(TURN) + spliter
                    dataOutput += str(RIVER)+ spliter
                    dataOutput += str(SB_TillNow + TMP_SB) + spliter
                    dataOutput += str(BB_TillNow + TMP_BB) + spliter
                    dataOutput += str(OpRaiseCount) + spliter
                    dataOutput += str(OpCallCount) + spliter
                    dataOutput += OpLastAction + "\n"
                    fileWriter.write(dataOutput)
                    print dataOutput
                pass
            pass

            SB_BB = GetStageMoney(actionSet[round], round)
            SB_TillNow += SB_BB[0]
            BB_TillNow += SB_BB[1]
            AllTillNow = SB_TillNow + BB_TillNow

    dataLine = fileReader.readline()
    lineCount += 1

print "----------------------------------------------------\nDone."