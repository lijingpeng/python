__author__ = 'lijingpeng'

# Generate ann input
# Global data
dataFile = "/home/lijingpeng/Public/annout.txt"
annDataFile = "/home/lijingpeng/Public/ann.txt"
spliter = ","

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


def CalcPokerHands(pokerhands, stage):
    a_count = 0 # done
    pair_ct = 0
    three_c = 0
    fourh_c = 0
    flush_c = 0
    #strai_p = 0

    number = {}
    flower = {}
    print "pokerhands",pokerhands
    # calc
    for i in range( len(pokerhands) ):
        if i % 2 == 0: # poker number
            if number.has_key(pokerhands[i]):
                number[ pokerhands[i] ] += 1
            else:
                number[ pokerhands[i] ] = 1
            pass
            if pokerhands[i] == "A":
                a_count += 1
            pass
        else:           # flower
            if flower.has_key(pokerhands[i]):
                flower[ pokerhands[i] ] += 1
            else:
                flower[ pokerhands[i] ] = 1
            pass
    pass

    ## traverse dict
    for num in number.keys():
        if number[num] > 1:
            pair_ct += 1
        elif number[num] >= 3:
            three_c += 1
        elif number[num] == 4:
            fourh_c = 1
        else:
            pass
    pass

    ## traverse flower dict
    for fl in flower.keys():
        if flower[fl] > flush_c:
            flush_c = flower[fl]


    print "a_C", a_count
    print "pair", pair_ct
    print "three", three_c
    print "four", fourh_c
    print "flush_c",flush_c
    print number
    print flower
    retVal = []
    retVal += [a_count]
    retVal += [pair_ct]
    retVal += [three_c]
    retVal += [fourh_c]
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

while dataLine and lineCount < 20:
    #line sb win opokers actions oactions
    #1#0#0#3h8s#rf#r
    #2#1#0#AsTd|QhTs2d|2c|Jc#rc/crrc/rc/rc#c|cr|r|r
    dataLine = dataLine.strip("\n")
    dataPiece = dataLine.split("#")
    pokerHand = dataPiece[3].split("|")
    actionSet = dataPiece[4].split("/")
    if dataPiece[1] == "0" and dataPiece[5] == "f":
        dataLine = fileReader.readline()
        lineCount += 1
        continue
    print "org", lineCount, "->", dataLine
    print "poker_hand", pokerHand

    index = 0
    FLOP = 0
    TURN = 0
    RIVER = 0
    OpRaiseCount = 0
    OpCallCount = 0
    SB_TillNow = 0
    BB_TillNow = 0
    OpLastAction = ""
    #
    A_Count = 0
    Pair_Count = 0
    Flush_Possible = 0
    Straight_Possible = 0
    Three_kind = 0
    Four_kind = 0

    ######################################################### pre-flop
    if dataPiece[1] == "1": # i am small, op big
        for i in range(len(actionSet[0])):
            ### hand poker
            #hands = list( pokerHand[0] )
            #CalcPokerHands(hands)
            ###################
            if i % 2 == 0: # "me"
                actionList = list(actionSet[0][:i])
                SB_BB = GetStageMoney(actionList, 0)
                SB_TillNow = SB_BB[0]
                BB_TillNow = SB_BB[1]
                FLOP = 0
                TURN = 0
                RIVER = 0
                RA_CA = GetRaiseCallCount(actionList, 0, 0)
                #OpRaiseCount = RA_CA[0]
                #OpCallCount = RA_CA[1]
                if i >= 1:
                    OpLastAction = actionList[i - 1]
                pass

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
                dataOutput += str(OpRaiseCount + RA_CA[0]) + spliter
                dataOutput += str(OpCallCount + RA_CA[1]) + spliter
                dataOutput += OpLastAction + spliter
                dataOutput += list(actionSet[0])[i] + "\n"
                fileWriter.write(dataOutput)
                #print dataOutput
        RA_CA = GetRaiseCallCount(actionSet[0], 0, 0)
        OpRaiseCount += RA_CA[0]
        OpCallCount  += RA_CA[1]
        #if len(actionSet[0]) % 2 == 0: # even 2 problem
        #    OpCallCount += 1
        #pass
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
                #OpRaiseCount = RA_CA[0]
                #OpCallCount = RA_CA[1]
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
                dataOutput += str(OpRaiseCount + RA_CA[0]) + spliter
                dataOutput += str(OpCallCount + RA_CA[1]) + spliter
                dataOutput += OpLastAction + spliter
                dataOutput += list(actionSet[0])[i] + "\n"
                fileWriter.write(dataOutput)
                #print dataOutput
        pass
        RA_CA = GetRaiseCallCount(actionSet[0], 1, 0)
        OpRaiseCount += RA_CA[0]
        OpCallCount  += RA_CA[1]
        #if len(actionSet[0]) % 2 != 0: # odd 1 problem
        #    OpCallCount += 1
        #pass
    pass

    SB_BB = GetStageMoney(actionSet[0], 0)
    SB_TillNow = SB_BB[0]
    BB_TillNow = SB_BB[1]
    AllTillNow = SB_TillNow + BB_TillNow

######################################################################################## after
    if dataPiece[1] == "1": # i am small, op big 0 2
        for round in range(1, len(actionSet), 1): #####ignore pre-flop
            pokers = []
            for po in range(0, round, 1):
                pokers += pokerHand[po]
            pokers += pokerHand[round]
            CalcPokerHands(pokers, round)
            for i in range(len(actionSet[round])):
                if i % 2 != 0: # "me"
                    TMP_SB = 0
                    TMP_BB = 0
                    actionList = list(actionSet[round][:i])
                    SB_BB = GetStageMoney(actionList, round)
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
                    pass
                    TMP_RC = 0
                    TMP_CC = 0
                    RA_CA = GetRaiseCallCount(actionList, 0, round)
                    #TMP_RC = RA_CA[0]
                    #TMP_CC = RA_CA[1]
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
                    dataOutput += str(OpRaiseCount + RA_CA[0]) + spliter
                    dataOutput += str(OpCallCount + RA_CA[1]) + spliter
                    dataOutput += OpLastAction + spliter
                    dataOutput += list(actionSet[round])[i] + "\n"
                    fileWriter.write(dataOutput)
                    #print dataOutput
                pass
            pass

            RA_CA = GetRaiseCallCount(actionSet[round], 0, round)
            OpRaiseCount += RA_CA[0]
            OpCallCount  += RA_CA[1]
            #if len(actionSet[round - 1]) % 2 != 0 and round > 1:
            #    OpCallCount += 1
            #pass
            SB_BB = GetStageMoney(actionSet[round], round)
            SB_TillNow += SB_BB[0]
            BB_TillNow += SB_BB[1]
            AllTillNow = SB_TillNow + BB_TillNow
        pass
    else: ## i am big, op big 1 3
        for round in range(1, len(actionSet), 1): #####ignore pre-flop
            for i in range(len(actionSet[round])):
                if i % 2 == 0: # "me"
                    TMP_SB = 0
                    TMP_BB = 0
                    actionList = list(actionSet[round][:i])
                    SB_BB = GetStageMoney(actionList, round)
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
                    RA_CA = GetRaiseCallCount(actionList, 1, round)
                    #OpRaiseCount += RA_CA[0]
                    #OpCallCount += RA_CA[1]
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
                    dataOutput += str(OpRaiseCount + RA_CA[0]) + spliter
                    dataOutput += str(OpCallCount + RA_CA[1]) + spliter
                    dataOutput += OpLastAction + spliter
                    dataOutput += list(actionSet[round])[i] + "\n"
                    fileWriter.write(dataOutput)
                    #print dataOutput
                pass

            RA_CA = GetRaiseCallCount(actionSet[round], 1, round)
            OpRaiseCount += RA_CA[0]
            OpCallCount  += RA_CA[1]
            #if len(actionSet[round - 1]) % 2 == 0 and round > 1:
            #    OpCallCount += 1
            #pass

            SB_BB = GetStageMoney(actionSet[round], round)
            SB_TillNow += SB_BB[0]
            BB_TillNow += SB_BB[1]
            AllTillNow = SB_TillNow + BB_TillNow
        pass
    pass

    dataLine = fileReader.readline()
    lineCount += 1
pass # while

print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nDone."