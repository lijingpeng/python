'''
Created on 2013-4-19

@author: hadoop
'''

if __name__ == '__main__':
    pass

import Image
import matplotlib.pyplot as plt
import numpy as np
import math
import copy as cp

def sortedDictValues(adict):
    items = adict.items()
    items.sort()
    return [value for key, value in items]

def AddAll(data, start, end):
    sum = 0.0
    for i in range(start, end, 1):
          sum += data[i]

    return sum

def MaxLevel(data):
    temp = data[0]
    maxi = 255
    for i in range(256):
        if data[i] >= temp:
            temp = data[i]
            maxi = i

    return maxi

def MinLevel(data):
    temp = data[0]
    mini = 0
    for i in range(256):
        if data[i] < temp:
            temp = data[i]
            mini = i

    return mini

def HistOne(datalist, w, h):
    temp = []
    for i in range(256):
        temp.append( datalist[i] / (w * h) )

    return temp

def GetHistData(array, w, h):
    dicR = {}
    for i in range(256):
        dicR[i] = 0
    dicG = {}
    for i in range(256):
        dicG[i] = 0
    dicB = {}
    for i in range(256):
        dicB[i] = 0
    for i in range(w):
        for j in range(h):
            if dicR.has_key(array[i][j][0]):
                dicR[array[i][j][0]] += 1
    for i in range(w):
        for j in range(h):
            if dicG.has_key(array[i][j][1]):
                dicG[array[i][j][1]] += 1
    for i in range(w):
        for j in range(h):
            if dicB.has_key(array[i][j][2]):
                dicB[array[i][j][2]] += 1

    dicR = sortedDictValues(dicR)
    dicG = sortedDictValues(dicG)
    dicB = sortedDictValues(dicB)
    histdata = []
    for i in range(256):
         histdata.append( dicR[i]*0.30 + dicG[i]*0.59 + dicB[i]*0.11 )

    return histdata

def HistAvg(histlist, w ,h, dataset):
    tmpData = cp.copy(dataset)
    tmp = HistOne(histlist, w, h)
    listold = []
    for i in range(256):
        listold.append(AddAll(tmp, 0, i))

    max = MaxLevel(histlist)
    min = MinLevel(histlist)

    for i in range(w):
        for j in range(h):
            tmpData[i][j][2] = listold[dataset[i][j][2]] * (max - min) + min

    return tmpData

def RGBtoHSI(rgb, wii, hii):
    HSISet = cp.copy(rgb)
    HSISet = HSISet.astype(float);
    for pi in range(wii):
        for pj in range(hii):
            sumRGB = int(rgb[pi][pj][0]) + int(rgb[pi][pj][1]) + int(rgb[pi][pj][2])
            sumRGB = float(sumRGB)
            r = 0
            g = 0
            b = 0
            if sumRGB != 0:
                r = rgb[pi][pj][0] / sumRGB
                g = rgb[pi][pj][1] / sumRGB
                b = rgb[pi][pj][2] / sumRGB

            mf =  ( ( (r-g)*(r-g) + (r-b)*(g-b) ) )**0.5
            factor = 0.0
            if mf != 0:
                factor = math.acos( (0.5*(r+r-g-b)) / mf )

            if b <= g:
                h = factor
            else:
                h = 6.28 - factor

            min = r
            if min > g:
                min = g
            if min > b:
                min = b

            s = 1 - 3 * min
            i = sumRGB / (3 * 255)

            H = h * 180 / 3.14
            S = s * 100
            I = i * 255

            HSISet[pi][pj][0] = H #H [0 360]
            HSISet[pi][pj][1] = S #S [0 100}
            HSISet[pi][pj][2] = I  #[0 255]

    return HSISet

def HSItoRGB(hsi, wii, hii):
    RGBSet = cp.copy(hsi)
    RGBSet = RGBSet.astype(float);
    print 'ff', RGBSet
    for pi in range(wii):
        for pj in range(hii):
            h = (hsi[pi][pj][0]*3.14/180)
            s = (hsi[pi][pj][1]/100.0)
            i = (hsi[pi][pj][2]/255.0)
            #print h,s,i
            r = 0
            g = 0
            b = 0

            if h < 2.1:
                x = i * (1 - s)
                y = i * ( 1 + s*math.cos(h)/math.cos(1.047 - h) )
                z = 3*i - x -y
                b = x; r = y; g = z
            if h>=2.1 and h<=4.19:
                h = h - 2.1
                x = i * (1 - s)
                y = i * ( 1 + s*math.cos(h)/math.cos(1.047 - h) )
                z = 3*i - x -y
                r = x; g = y; b = z
            if h>4.19 and h<6.28:
                h = h - 4.19
                x = i * (1 - s)
                y = i * ( 1 + s*math.cos(h)/math.cos(1.047 - h) )
                z = 3*i - x -y
                g = x; b = y; r = z

            RGBSet[pi][pj][0] = r * 255
            RGBSet[pi][pj][1] = g * 255
            RGBSet[pi][pj][2] = b * 255

    return RGBSet

def DrawHist(data):
    #plt.axis([0,255,0,2000])
    #print len(data)
    plt.plot(data)
    plt.title('Histogram of '+filename)
    plt.xlabel('Level')
    plt.show()

#-----------------------------------Main------------------------------------
filename = 'lina.bmp'
img = Image.open(filename)
#img.show()
imgsize = img.size
RGBData = np.array(img)

HSIdata = RGBtoHSI(RGBData, imgsize[0], imgsize[1])
intHSIData = HSIdata.astype(int);


histData = GetHistData(RGBData, imgsize[0], imgsize[1])
#print intHSIData
afterHistAvg = HistAvg(histData, imgsize[0], imgsize[1], intHSIData)
#print 'ag--',afterHistAvg
print '---------------------------------------------------------------------'
ReConvertRGB = HSItoRGB(afterHistAvg, imgsize[0], imgsize[1])
ReConvertRGB = ReConvertRGB.astype(int);

resHist = GetHistData(ReConvertRGB, imgsize[0], imgsize[1])
DrawHist(resHist)

print ReConvertRGB
plt.imshow(ReConvertRGB)
plt.show()
#print RGBData
#print RGBData


#print HSIdata
#print intHSIData
print '---------------------------------------------------------------------'
#ReConvertRGB = HSItoRGB(HSIdata, imgsize[0], imgsize[1])
#print ReConvertRGB
#print HSIdata
#HSIArray = np.array( HSIList )
#print HSIArray
#After = np.array( HSItoRGB(HSIArray, imgsize[0], imgsize[1]) )
#print After

