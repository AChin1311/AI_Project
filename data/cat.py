#-*- encoding:utf-8 -*-#
import json
import random
import sys

if len(sys.argv) <= 2:
    print("Usage: python cat.py <json-file> ... <json-file> <output-file>")
    exit(0)

dlist = sys.argv[1:-1]
acc = []
for data in dlist:
    acc += json.load(open(data, "r"))
    print(acc)

#random.shuffle(acc)

json.dump(acc, open(sys.argv[-1], "w"), indent=2)
