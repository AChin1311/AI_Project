#-*- encoding: utf-8 -*-
import json
import requests
import sys
import time
import config
from instagram.client import InstagramAPI

token = config.token
social_media = [u"whatsapp", u"facebook", u"wechat", u"line"]
keywords = [u"$", u"購", u"禮", u"優惠", u"郵寄", u"價", u"面交", u"shop", u"sell"]
days = 5
api = InstagramAPI(access_token=token)

def search_by_tag(tag, count=20):
   url = "https://api.instagram.com/v1/tags/"+tag+"/media/recent?access_token="+token+"&count="+str(count)

   #while True:
   req = requests.get(url)
   jdata = json.loads(req.text)
   return jdata["data"]
   #url = jdata["pagination"]["next_url"]

def get_info(id):
    '''
    req = requests.get("https://api.instagram.com/v1/users/"+id+"/media/recent?min_timestamp="+str(int(time.time())-86400*days)+"&access_token="+token)
    
    if req.status_code == 200:
        last = len(json.loads(req.text)["data"])
    else:
        return "", 0, 0
    '''
    last = 0
    
    req = requests.get("https://api.instagram.com/v1/users/"+id+"?access_token="+token)
    
    jsond = json.loads(req.text)
    info = jsond["data"]["bio"]
    followby = jsond["data"]["counts"]["followed_by"]
    
    

    return info,last,max(followby, 0.001)

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

def features(post):
    out = []
    tag_amount = len(post["tags"])
    author_info, post_last, follower = get_info(post["user"]["id"])
    like = post["likes"]["count"]
    comment = post["comments"]["count"]
    content = post["caption"]["text"]
  
    #print(follower)
    out.append(tag_amount)
    out.append(like)
    out.append(comment)
    out.append(follower)
    out.append(post_last)
    #out += [0,0]

    out += matching(author_info)
    out += matching(content)

    return dict(enumerate(out))


