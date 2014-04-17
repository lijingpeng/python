__author__ = 'lijingpeng'

import os, shutil

# File source path
dataPaths = ["/home/data/ACPCData/2013/2pl_logs/"]
# Specific opponent
opponent = "zbot"
# destination
destination = "/home/data/2013/2pl/zbot_select/"

# Get all files in the path list
files = []
for path in dataPaths:
    files = files + os.listdir(path)
    # Get log files for specific opponent and store them in destination folder
    for filename in files:
        if filename.find( opponent ) != -1 and filename.find( "marv" ) != -1 :
            shutil.copyfile(path + filename, destination + filename)
        elif filename.find( opponent ) != -1 and filename.find("feste") != -1:
            shutil.copyfile(path + filename, destination + filename)
        elif filename.find( opponent ) != -1 and filename.find("hyperborean") != -1:
            shutil.copyfile(path + filename, destination + filename)
        #elif filename.find( opponent ) != -1 and filename.find("littlerock") != -1:
        #    shutil.copyfile(path + filename, destination + filename)
        #elif filename.find( opponent ) != -1 and filename.find("propokertools") != -1:
        #    shutil.copyfile(path + filename, destination + filename)
        else:
            pass
    pass
pass

print "Done."
