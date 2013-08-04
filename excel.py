#!/usr/bin/env python

import xlrd
import xlwt
from xlutils.copy import copy

Jbook = xlrd.open_workbook("D:\jj.xls")
Hbook = xlrd.open_workbook("D:\hh.xls")

Jsheet = Jbook.sheet_by_index(0)
Hsheet = Hbook.sheet_by_index(0)
WHbook = copy( Hbook )
WHsheet = WHbook.get_sheet(0)

HrowsN = Hsheet.nrows
JrowsN = Jsheet.nrows
print '½ðÁ¢ has ', HrowsN, ' Rows.'
n = 0

for i in range(1, HrowsN):
    Hkeydata = Hsheet.cell(i, 8).value
    # print Hkeydata, '\n'
    for j in range(1, JrowsN):
        Jkeydata = Jsheet.cell(j, 1).value, '\n'
        JkeydataStr = str(Jkeydata)
        # print JkeydataStr[1:11]
        if Hkeydata == JkeydataStr[1:11]:
            WHsheet.write(i, 0, Jsheet.cell(j, 0).value)
            # Htable.put_cell(i, 0, 2, Jtable.cell(j, 0).value, 0)
            n = n + 1    
            # print n, '\n'

print n, ' Rows modified.'
WHbook.save("llaas.xls")
