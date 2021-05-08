# Bad python code but it works
import glob
import os
import yaml
import json

paths = glob.glob("rehid/*/*/*/*/")
games = glob.glob("rehid/*/")
names = []
for game in games:
    names.append(os.path.basename(os.path.normpath(game)))
tidlist = {}
i = 0
for game in games:
    tidl = {"EUR":0, "USA":0, "JPN":0, "TWN":0, "AU":0, "KR":0}
    for regions in glob.glob(game + "*/"):
        tids = glob.glob(regions + "rehid/*/")
        if len(tids) == 0:
            tids = glob.glob(regions + "/*/")
        l = []
        for tid in tids:
            l.append(os.path.basename(os.path.normpath(tid)))
        tidl[os.path.basename(os.path.normpath(regions))] = l
    tidlist[names[i]] = tidl
    i = i + 1

jsonfile = open("titlelist.json", "w")
json.dump(tidlist, jsonfile, indent=4)
jsonfile.close()
######