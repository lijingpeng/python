__author__ = 'lijingpeng'

import os, shutil

# File source path
dataPaths = ["/home/data/ACPCData/2013/2pl_logs/"]
# Specific opponent
opponent = "marv"
# destination
destination = "/home/lijingpeng/Public/tmp/"

# Get all files in the path list
files = []
for path in dataPaths:
    files = files + os.listdir(path)
    # Get log files for specific opponent and store them in destination folder
    for filename in files:
        if filename.find( opponent ) != -1:
            shutil.copyfile(path + filename, destination + filename)

print "Done."