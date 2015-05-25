#-*- encoding:utf-8 -*-
import json
import requests
import sys
import time
import config
from multiprocessing import Pool

social_media = [u"whatsapp", u"facebook", u"wechat", u"line"]
keywords = [u"$", u"購", u"禮", u"優惠", u"郵寄", u"價", u"面交", u"shop", u"sell"]
token = config.token
days = 5

def get_info(id):
    req = requests.get("https://api.instagram.com/v1/users/"+id+"/media/recent?min_timestamp="+str(int(time.time())-86400*days)+"&access_token="+token)
    
    if req.status_code == 200:
        last = len(json.loads(req.text)["data"])
    else:
        return "", 0, 1000000000000000000 
    
    req = requests.get("https://api.instagram.com/v1/users/"+id+"?access_token="+token)
    
    jsond = json.loads(req.text)
    info = jsond["data"]["bio"]
    followby = jsond["data"]["counts"]["followed_by"]

    return info,last,max(followby, 0.001)

def matching(content):
    wcount = sum(map(lambda s: content.count(s) , keywords))
    solist = list(map(lambda s: s in content, social_media))
    solist.append(wcount)
    
    mx = 0
    now = 0
    for char in content:
        if char.isdigit():
            now += 1
        else:
            now = 0
        mx = max(mx, now)
    solist.append(mx)

    return solist
    

def main():

    if len(sys.argv) != 3:
        print("Usage: python json2libsvm.py <json-file> <data-file>")
        exit(0)

    fname = sys.argv[1]

    data = json.load(open(fname, "r"))

    p = Pool(5)
    ret = p.map(func, data)

    fl = open(sys.argv[2], "w")
    for line in ret:
        fl.write(line+"\n")

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
    out.append(float(like)/follower)
    out.append(float(comment)/follower)
    out.append(post_last)

    out += matching(author_info)
    out += matching(content)

    label = "+1 " if label else "-1 "
    return label+" ".join(map(lambda z: "%d:%f" % (z[0]+1, z[1]), enumerate(out)))

if __name__ == "__main__":
    main()
