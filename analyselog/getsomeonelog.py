__author__ = 'lijingpeng'

import os, shutil

# File source path
dataPaths = ["/home/data/ACPCData/2013/2pl_logs/"]
# Specific opponent
opponent = "marv"
# destination
destination = "/home/lijingpeng/Public/ann/anndata/2pl2012_song_marv/"

# Get all files in the path list
files = []
for path in dataPaths:
    files = files + os.listdir(path)
    # Get log files for specific opponent and store them in destination folder
    for filename in files:
        if filename.find( opponent ) != -1 and filename.find( "HITSZ" ) != -1 :
            shutil.copyfile(path + filename, destination + filename)
        #elif filename.find( opponent ) != -1 and filename.find("hyperborean"):
        #    shutil.copyfile(path + filename, destination + filename)
        #elif filename.find( opponent ) != -1 and filename.find("zbot"):
        #    shutil.copyfile(path + filename, destination + filename)
        #elif filename.find( opponent ) != -1 and filename.find("littlerock"):
        #    shutil.copyfile(path + filename, destination + filename)
        #elif filename.find( opponent ) != -1 and filename.find("propokertools"):
        #    shutil.copyfile(path + filename, destination + filename)
        #else:
        #    pass
    pass
pass

print "Done."