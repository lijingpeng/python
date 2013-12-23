__author__ = 'lijingpeng'

# Generate ann input


# Global data
dataFile = "/home/lijingpeng/Public/annout.txt"
annDataFile = "/home/lijingpeng/Public/ann.txt"


def GetRaiseCount(opActions):
    Count = 0
    for i in opActions:
        if i == "r":
            Count += 1
    pass

    return Count
    pass

# get current stage money
# @actions : current action in specific stage
# @round : specify pre-flop or not
def GetStageMoney(actions, round):
    # rc
    sbTotal = 0
    bbTotal = 0
    raiseUnit = 10
    if round > 1:
        raiseUnit = 20
    else:
        raiseUnit = 10
    pass

    if round == 0:  # pre-flop round, small blind goes first
        sbTotal = 0
        bbTotal = 5
        for i in len(actions):
            # 0, 2, 4 for small blind
            # 1, 3 for big blind
            if actions[i] == "c": # call
                if i % 2 == 0: # sb
                    sbTotal += abs(bbTotal - sbTotal)
                else:   # bb
                    bbTotal += abs(bbTotal - sbTotal)
                pass
            elif actions[i] == "r":
                if i % 2 == 0: # bb
                    bbTotal += abs(bbTotal - sbTotal) + raiseUnit
                else:   # sb
                    sbTotal += abs(bbTotal - sbTotal) + raiseUnit
            else:
                pass
            pass
        pass
    else: # after pre-flop stage: big blind goes first
        sbTotal = 0
        bbTotal = 0
    pass

    retVal = []
    retVal += [ sbTotal ]
    retVal += [ bbTotal ]
    return retVal


# open output file
fileWriter = open(annDataFile, "w")
dataOutput = ""

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
    dataLine = dataLine.strip("\n")
    dataPiece = dataLine.split("#")

    # different stage
    stages = dataPiece[4].split("/")    # All action sequence
    opStages = dataPiece[5].split("|")  # opponent's action sequence
    roundCount = len(stages)
    # following variables are the input of the neural network
    FLOP = 0
    TURN = 0
    RIVER = 0
    OP_RAISE_COUNT = 0
    SB_TOTAL = 5            # initial small blind pot money
    BB_TOTAL = 2 * SB_TOTAL # initial big blind pot money
    POTALL = 15 # the money in the pot till now, once start the game, it is 15
    ME_SB = dataPiece[1] # 0 for big blind, 1 for small blind
    for i in range(0, roundCount, 1): # i will be 0,1,2,3; 0 will be valid, while 1,2,3 depends
        if i == 0: #stage 1 [pre-flop], FLOP = 0, TURN = 0, RIVER = 0
            FLOP = 0
            TURN = 0
            RIVER = 0
            OP_RAISE_COUNT += GetRaiseCount( [opStages[ i ]] )
            # Calc pot money

            print "raise", OP_RAISE_COUNT
        pass
    pass

    print dataPiece
    dataLine = fileReader.readline()
    lineCount += 1
    pass

print "----------------------------------------------------\nDone."