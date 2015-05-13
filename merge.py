import json
import sys

if len(sys.argv) != 4:
   print "Usage: ./merge.py <data> <label> <output>"

jsond = json.load(file(sys.argv[1]))
labels = json.load(file(sys.argv[2]))

for (i, x) in enumerate(jsond["data"]):
   x["label"] = labels[i]

json.dump(jsond, file(sys.argv[3], "w"), indent=2, separators=(',', ': '))
