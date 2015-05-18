import json
import random

dlist = ["cat.json", "doominjun.json", "food.json", "girl.json", "gudetama.json", "japan.json", "summer.json","taiwan.json"]

acc = []
for data in dlist:
    acc += json.load(open(data, "r"))

random.shuffle(acc)

json.dump(acc, open("out", "w"), indent=2)
