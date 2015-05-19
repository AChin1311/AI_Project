import json
import requests
import sys
import config

token = config.token
tag = sys.argv[1]
n = int(sys.argv[2])
j = []
url = "https://api.instagram.com/v1/tags/"+tag+"/media/recent?access_token="+token

while n > 0:
	req = requests.get(url)
	url = json.loads(req.text)["pagination"]["next_url"]
	j += json.loads(req.text)["data"]
	n -= 20

fname = tag+".json"
json.dump(j, open(fname, "w"), indent=2)