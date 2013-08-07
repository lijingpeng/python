#!bin/python
import Image as im
import numpy as np
import copy as cp

img = im.open('lina.bmp')
arr = np.array(img)
print arr

data = cp.copy(arr)
data[0][0][0]=111
print 'data:',data[0][0][0]
print 'arr:',arr[0][0][0]

