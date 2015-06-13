#-*- encoding: utf-8 -*-
import json
import requests
import sys
import time
import config

token = config.token
#bound = [(1, 59),(0, 4038),(0, 31),(0, 102750),(0, 20),(0, 9),(0, 3),(0, 12),(0, 34),(0, 7),(0, 20)]
#bound = [(1,59),(0,4038),(0,31),(0,105243),(0,20),(0,10),(0,3),(0,12),(0,42),(0,41),(0,7),(0,20),(0,97),(0,1),(0,31)]

bound = {}
lower, upper = -1, 1
social_media = [u"whatsapp", u"facebook", u"wechat", u"line"]
#keywords = [u"日本", u"現貨", u"減肥", u"禮物", u"您", u"公仔", u"買", u"優惠", u"歡迎", u"請", u"查詢", u"韓國", u"面交", u"生日", u"情侶", u"門市", u"禮", u"惠", u"賣", u"購"]

keywords = [u'個', u'卡龍', u'日本', u'香水', u'來', u'效果', u'到', u'五月天', u'是', u'優惠', u'女神', u'香港', u'袋', u'唔', u'的', u'後', u'一個', u'交收', u'月', u'不', u'直送', u'鍊', u'呢', u'情侶', u'全新', u'好', u'夏天', u'所有', u'面', u'年', u'送', u'啲', u'迪士尼', u'都', u'為', u'面交', u'已經', u'要', u'手', u'發售', u'褲', u'寄', u'睇', u'手鏈', u'以下', u'等', u'男', u'買', u'你', u'門 市', u'啦', u'會', u'又', u'回覆', u'保證', u'正妹', u'蔬菜', u'同', u'用', u'有', u'既', u'努力', u'早安', u'最', u'去', u'飯', u'歡迎', u'公仔', u'有意', u'您', u'做', u'蛋黃哥', u'咩', u'訂貨', u'節', u'韓國', u'健康', u'平', u'紙膠', u'下', u'聯絡', u'自己', u'情人', u'了', u'古', u'使用', u'現貨', u'人', u'特價', u'長', u'絕對', u'呀', u'戒指', u'查詢', u'龍貓', u'訂購', u'就', u'敏俊', u'減肥', u'精華', u'帶', u'冇', u'型', u'瘦身', u'可', u'代購', u'韓國代購', u'母親節', u'我們', u'鈪', u'旺角', u'豐胸', u'和', u'或', u'費洛蒙', u'生日', u'時', u'女裝', u'好評', u'裙', u'貨品', u'可愛', u'隻', u'得', u'電話', u'在', u'對', u'禮物', u'係', u'東京', u'運動', u'信', u'可以', u'地', u'一', u'吃', u'復', u'店主', u'台灣', u'黏土', u'我', u'瘦面', u'馬', u'髮', u'請']

keychars = [u'唔', u'運', u'風', u'張', u'家', u'預', u'膚', u'式', u'潮', u'即', u'你', u'蔬', u'貓', u'盒', u'做', u'護', u'動', u'我', u'白', u'糕', u'首', u'多', u'對', u'情', u'速', u'早', u'香', u'中', u'查', u'卡', u'要', u'訂', u'己', u'物', u'腳', u'條', u'款', u'買', u'您', u'比', u'品', u'質', u'直', u'膠', u'親', u'種', u'少', u'其', u'正', u'帶', u'減', u'靚', u'店', u'心', u'母', u'如', u'左', u'作', u'趣', u'紙', u'成', u'實', u'交', u'特', u'福', u'歡', u'素', u'高', u'係', u'黏', u'部', u'自', u'年', u'內', u'臉', u'五', u'制', u'迎', u'能', u'念', u'令', u'長', u'次', u'電', u'點', u'滿', u'韓', u'功', u'上', u'小', u'會', u'鈪', u'好', u'士', u'證', u'復', u'洛', u'每', u'意', u'為', u'環', u'完', u'寄', u'菜', u'俊', u'星', u'萬', u'清', u'皮', u'購', u'呀', u'現', u'金', u'線', u'絡', u'銀', u'版', u'感', u'飾', u'發', u'們', u'重', u'兩', u'啲', u'背', u'得', u'鍊', u'袋', u'連', u'瘦', u'場', u'提', u'推', u'不', u'子', u'洗', u'顏', u'套', u'鞋', u'支', u'市', u'康', u'妹', u'謝', u'蒙', u'就', u'呢', u'仙', u'行', u'折', u'設', u'拍', u'太', u'南', u'雪', u'型', u'過', u'到', u'經', u'期', u'蛋', u'迪', u'性', u'話', u'日', u'假', u'頸', u'肥', u'鐵', u'數', u'一', u'件', u'覺', u'以', u'髮', u'想', u'油', u'持', u'貨', u'保', u'修', u'吃', u'新', u'收', u'主', u'覆', u'系', u'月', u'仲', u'在', u'代', u'灣', u'古', u'化', u'了', u'都', u'三', u'馬', u'沒', u'或', u'個', u'肉', u'花', u'加', u'水', u'禮', u'粉', u'優', u'美', u'狗', u'朋', u'回', u'使', u'布', u'可', u'請', u'無', u'全', u'大', u'寬', u'之', u'體', u'華', u'人', u'友', u'裙', u'冇', u'放', u'腿', u'丸', u'防', u'手', u'隻', u'產', u'青', u'脂', u'是', u'黑', u'評', u'擇', u'份', u'別', u'節', u'指', u'黎', u'去', u'底', u'他', u'問', u'座', u'包', u'服', u'有', u'地', u'面', u'哥', u'公', u'最', u'信', u'熱', u'衫', u'藍', u'專', u'本', u'留', u'合', u'港', u'眼', u'量', u'尼', u'龍', u'備', u'男', u'貼', u'選', u'波', u'免', u'先', u'胸', u'食', u'短', u'分', u'來', u'色', u'單', u'郵', u'牛', u'強', u'生', u'流', u'神', u'健', u'文', u'已', u'紀', u'黃', u'寶', u'約', u'夏', u'筆', u'只', u'枝', u'褲', u'售', u'聯', u'工', u'者', u'頭', u'業', u'入', u'餐', u'號', u'角', u'耳', u'台', u'鏈', u'戒', u'力', u'季', u'及', u'需', u'腰', u'春', u'圖', u'增', u'定', u'衣', u'又', u'紅', u'由', u'真', u'東', u'妝', u'裝', u'緊', u'糯', u'米', u'國', u'理', u'幫', u'時', u'均', u'飯', u'天', u'二', u'快', u'既', u'肌', u'價', u'侶', u'土', u'間', u'的', u'味', u'女', u'限', u'努', u'方', u'身', u'等', u'同', u'咩', u'送', u'開', u'睇', u'阿', u'外', u'門', u'更', u'平', u'詢', u'甲', u'然', u'所', u'精', u'毛', u'效', u'和', u'下', u'仔', u'容', u'補', u'接', u'後', u'敏', u'引', u'明', u'出', u'站', u'愛', u'用', u'啦', u'費', u'機', u'惠', u'京', u'絕', u'豐', u'超', u'旺', u'相', u'營', u'原', u'果', u'安']


days = 20

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
    info = jsond["data"]["full_name"]+jsond["data"]["bio"]
    followby = jsond["data"]["counts"]["followed_by"]
    print(followby) 
    return info,last,max(followby, 0.001)

def matching(content):
    
    content = content.replace(" ", "").replace("-", "").lower()

    
    li = []
    for cha in keychars:
        cnt = content.count(cha)
        li.append(cnt)

    for word in keywords:
        cnt = content.count(word)
        if cnt != 0:
            print(word)
        li.append(cnt)

    #wcount = sum(map(lambda s: content.count(s) , keywords))
    socount = sum(map(lambda s: content.count(s), social_media))
    #li = [wcount, socount]
    li.append(socount)

    mx = 0
    now = 0
    total = 0
    for char in content:
        if char.isdigit():
            now += 1
            total += 1
        else:
            now = 0
        mx = max(mx, now)
    li += [mx, total]

    return li

def features(post, scl = True):
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
    out.append(0 if post["filter"] == "Normal" else 1)
    out.append(post["comments"]["count"])

    if scl == False:
        return out
   
    for i, val in enumerate(out):
        out[i] = scale(i+1, val)
    return out
    #return map(scale, zip(out, bound))

def scale(i, val):
    if not i in bound:
        return lower
    lb, ub = bound[i]
    return lower + (upper-lower) * (float(val) / (ub - lb))

def load_bound(bound_path):
    f = open(bound_path, "r")
    f.readline()

    lower, upper = f.readline().split(' ')
    lower, upper = int(lower), int(upper)
    
    for line in f:
        idx, lb, ub = line.split(' ')
        idx, lb, ub = int(idx), int(lb), int(ub)
        bound[idx] = (lb, ub)
