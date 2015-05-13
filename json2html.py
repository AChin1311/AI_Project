from html import HEAD, TAIL
import sys
import json

jsond = json.load(file(sys.argv[1]))
out = []

'''
for post in jsond["data"]:
   out.append({
      "link": post["images"]["low_resolution"]["url"],
      "text": post["caption"]["text"].replace("\n", "<br>")
   })
'''
f = open("train.html", "w")
f.write(HEAD)
f.write(json.dumps(jsond))
f.write(TAIL)
