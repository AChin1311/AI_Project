#-*- encoding: utf-8 -*-
import json
import requests
import sys
import time
import config

token = config.token
social_media = [u"whatsapp", u"facebook", u"wechat", u"line"]
keywords = [u"$", u"購", u"禮", u"優惠", u"郵寄", u"價", u"面交", u"shop", u"sell"]
days = 5
bound = []

def search_by_tag(tag, count=20, max_tag_id=None):
   url = "https://api.instagram.com/v1/tags/"+tag+"/media/recent?access_token="+token+"&count="+str(count)
   if max_tag_id:
      url += "&max_tag_id="+max_tag_id

   #while True:
   req = requests.get(url)
   jdata = json.loads(req.text)
   return jdata["data"], jdata["pagination"]["next_max_tag_id"]
      #url = jdata["pagination"]["next_url"]

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

def matching(content):
    
    content = content.replace(" ", "").replace("-", "").lower()

    wcount = sum(map(lambda s: content.count(s) , keywords))
    socount = sum(map(lambda s: content.count(s), social_media))
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
    content = post["caption"]["text"] if post["caption"] else ""
  
    out.append(tag_amount)
    out.append(like)
    out.append(comment)
    out.append(follower)
    out.append(post_last)

    out += matching(author_info)
    out += matching(content)

    return map(scale, zip(out, bound))

def scale(x):
   ft, (lb, ub) = x
   return -1 + 2 * (ft / (ub - lb))

