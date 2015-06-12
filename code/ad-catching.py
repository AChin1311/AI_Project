#-*- encoding: utf-8 -*-
import json
import requests
import sys
import jieba

'''
filename = [u"夏天.json", u"羊駝.json", u"五月天.json", u"夜景.json", u"生日快樂.json",
			u"天氣.json", u"蔬菜.json", u"母親節.json", u"廢話.json", u"貓咪.json",
			u"腳踏車.json", u"哭.json", u"文青.json", u"運動.json", u"蛋黃哥.json",
			u"人生.json", u"日本.json", u"閃光.json", u"迪士尼.json", u"可愛.json",
			u"早安.json", u"香港.json", u"都敏俊.json", u"台灣.json", u"正妹.json",
	       	u"髮型.json", u"馬卡龍.json", u"吃飯.json", u"海邊.json", u"龍貓.json" ]
'''
#filename = [u"文青.json", u"日本.json", u"母親節.json", u"吃飯.json", u"龍貓.json", u"早安.json", u"蔬菜.json", u"都敏俊.json", u"蛋黃哥.json", u"夏天.json", u"五月天.json", u"運動.json", u"髮型.json", u"馬卡龍.json", u"台灣.json", u"正妹.json"]
filename = ["960.train.json"]
dictionary = {}
L = []
data_path = "../data/"

for fn in filename:
    print (fn)
    data = json.load(open(data_path+fn, "r"))
    for d in data:
        if d["label"] != -1:
            text = d["caption"]["text"]
            words = jieba.cut(text, cut_all=False)
            #print(words)
            words = text
            for word in words:
                chinese = True
                for ch in word:
                    if ord(ch) < 0x4e00 or ord(ch) > 0x9fff:
                        chinese = False
                        break
                if chinese:
                    #print(word)
                    if word in dictionary:
                        dictionary[word] += 1
                    else:
                        dictionary[word] = 1 
            #print (word)

L2 = []
for word in dictionary:
    if dictionary[word] > 50:
        L.append((word, dictionary[word]))
        L2.append(word)
L.sort(key=lambda p: p[1])
print(L)	        
print(L2)


