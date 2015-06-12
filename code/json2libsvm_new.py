#-*- encoding:utf-8 -*-
import json
import requests
import sys
import time
import config
import util
from multiprocessing import Pool
from functools import partial

#social_media = [u"whatsapp", u"facebook", u"wechat", u"line"]
#keywords = [u"$", u"購", u"禮", u"優惠", u"郵寄", u"價", u"面交", u"shop", u"sell"]
#token = config.token
#days = 5

'''
def get_info(id):
    req = requests.get("https://api.instagram.com/v1/users/"+id+"/media/recent?min_timestamp="+str(int(time.time())-86400*days)+"&access_token="+token)
    
    if req.status_code == 200:
        last = len(json.loads(req.text)["data"])
    else:
        return "", 0, 0 
    
    req = requests.get("https://api.instagram.com/v1/users/"+id+"?access_token="+token)
    
    jsond = json.loads(req.text)
    info = jsond["data"]["bio"]
    followby = jsond["data"]["counts"]["followed_by"]

    return info,last,max(followby, 0.001)
'''

'''
def matching(content):
    
    content.replace(" ", "")
    content.replace("-", "")

    wcount = sum(map(lambda s: content.count(s) , keywords))
    socount = sum(map(lambda s: s in content, social_media))
    li = [wcount, socount]
    
    mx = 0
    now = 0
    for char in content:
        if char.isdigit():
            now += 1
        else:
            now = 0
        mx = max(mx, now)
    li.append(mx)

    return li
''' 

def main():

    if len(sys.argv) != 3:
        print("Usage: python json2libsvm.py <json-file> <data-file>")
        exit(0)

    fname = sys.argv[1]

    data = json.load(open(fname, "r"))

    p = Pool(3)
    #ret = p.map(util.features, zip(data, False)
    ret = p.map(partial(util.features, scl = False), data)
    p.close()
    p.join()
    
    fl = open(sys.argv[2], "w")
    for da,fe in zip(data, ret):
        lab = "+1 " if da["label"] else "-1 "
        fl.write(lab+" ".join(map(lambda z: "%d:%f" % (z[0]+1, z[1]), enumerate(fe)))+"\n")

'''
def func(post):
    out = []
    print(post)
    label = post["label"]
    tag_amount = len(post["tags"])
    author_info, post_last, follower = get_info(post["user"]["id"])
    like = post["likes"]["count"]
    comment = post["comments"]["count"]
    content = post["caption"]["text"]
  
    print(follower)
    out.append(tag_amount)
    out.append(like)
    out.append(comment)
    out.append(follower)
    out.append(post_last)

    out += util.matching(author_info)
    out += util.matching(content)

    label = "+1 " if label else "-1 "
    return label+" ".join(map(lambda z: "%d:%f" % (z[0]+1, z[1]), enumerate(out)))
'''

if __name__ == "__main__":
    main()
