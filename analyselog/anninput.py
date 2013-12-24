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
    #3#0#1#QsJs#f#f
    #4#1#1#JsQs|6dQd9h#rc/crf#c|cf
    #5#0#0#TdKs|Jd4c8s|Ac|2c#rc/crc/cc/crc#r|r|c|r
    #6#1#0#Kd4s|Kc6sAd|Ac|9h#rrc/rc/rc/rc#r|r|r|r
    #7#0#0#Qd7c|4h9s8s|4s#rc/cc/crf#r|c|r
    #8#1#0#Th2h|Ad4d3d|8d#rc/crrc/rf#c|cr|r
    #9#0#0#QhJd|5hAs6c|Tc|Th#rc/crc/crc/crc#r|r|r|r
    dataLine = dataLine.strip("\n")
    dataPiece = dataLine.split("#")
    print dataPiece
    # different stage
    stages = dataPiece[4].split("/")    # All action sequence
    opStages = dataPiece[5].split("|")  # opponent's action sequence
    roundCount = len(stages)
    # following variables are the input of the neural network
    FLOP = 0
    TURN = 0
    RIVER = 0
    OP_RAISE_COUNT = 0
    SB_TOTAL = 0 # initial small blind pot money
    BB_TOTAL = 0 # initial big blind pot money
    POTALL = 15 # the money in the pot till now, once start the game, it is 15
    ME_SB = dataPiece[1] # 0 for big blind, 1 for small blind
    for i in range(0, roundCount, 1): # i will be 0,1,2,3; 0 will be valid, while 1,2,3 depends
        if i == 0: #stage 1 [pre-flop], FLOP = 0, TURN = 0, RIVER = 0
            FLOP = 0
            TURN = 0
            RIVER = 0
            # for every single action, generate an output
            if dataPiece[0] == "0": # i am big blind, he goes first
                currentActions = list(stages[0])
                acTmp = []
                for j in range(len(stages[i])):
                    acTmp += currentActions[j]
                    dataOutput = ""
                    dataOutput += str(FLOP)             # 1. FLOP
                    dataOutput += str(TURN)             # 2. TURN
                    dataOutput += str(RIVER)            # 3. RIVER
                    dataOutput += str( GetRaiseCountStage(stages[i], 0, 0) )    # 4. until now, opponent raise count
                    sb_bb = GetStageMoney(acTmp, 0)
                pass
            else:                   # i am small blind
                pass
            OP_RAISE_COUNT += GetRaiseCount( [opStages[ i ]] )
            # Calc pot money
            stagePot = GetStageMoney(list( stages[i] ), i)
            SB_TOTAL += stagePot[0]
            BB_TOTAL += stagePot[1]
            print SB_TOTAL, BB_TOTAL

            print "raise", OP_RAISE_COUNT
        pass
    pass


    dataLine = fileReader.readline()
    lineCount += 1
    pass

print "----------------------------------------------------\nDone."