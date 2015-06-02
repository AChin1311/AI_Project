#-*- encoding: utf-8 -*-
import sys
import tornado.ioloop
import tornado.web
import util
import json
from multiprocessing import Pool
import os
#sys.path.append("./liblinear-1.96/python")
#import liblinearutil as liblr

#m = liblr.load_model("./10.model")

class Media:
   def __init__(self, media):
      self.url = media["images"]["low_resolution"]["url"]
      self.user = media["user"]["username"]
      self.post = media["caption"]["text"] if media["caption"] else ""
      self.post = self.post[:100]

class AjaxHandler(tornado.web.RequestHandler):
   def get(self, tag, max_tag_id):
      print tag
      p = Pool(10)

      medias, next_ = util.search_by_tag(tag, 3, max_tag_id)

      fs = p.map(util.features, medias)

      medias = map(lambda m: Media(m).__dict__, medias)

      self.write(json.dumps({
         "max_tag_id": next_,
         "medias": medias
       }))
      
      p.close()
      p.join()

class MainHandler(tornado.web.RequestHandler):
   def get(self, tag="貓咪"):
      p = Pool(10)
      if tag == "":
         return
      medias, next_ = util.search_by_tag(tag, 5)

      fs = p.map(util.features, medias)

      medias = map(lambda m: Media(m), medias)
      self.render("main.html", medias=medias, tag_name=tag, max_tag_id=next_)
      p.close()
      p.join()
      
application = tornado.web.Application([
      (r"/", MainHandler),
      (r"/ajax/(.+)/(.+)", AjaxHandler),
      (r"/(.+)", MainHandler),
   ],
   template_path=os.path.join(os.path.dirname(__file__), "template")
)

if __name__ == "__main__":
   application.listen(8888)
   tornado.ioloop.IOLoop.instance().start()
