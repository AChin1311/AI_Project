import json
import requests
import sys

fname = sys.argv[1] + ".json"
jsond = json.load(file(fname))
countyes = 0
countno = 0

for data in jsond:
    if data["label"] == 1:
        countyes += 1
    else:
        countno += 1

f = open("data_info", "a")
f.write(sys.argv[1] + " Ad: " + str(countyes) + " NotAd: " + str(countno) + "\n")
