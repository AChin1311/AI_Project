#*- encoding: utf-8 -*-
import sys
import tornado.ioloop
import tornado.web
import util
import json
from multiprocessing import Pool
import os
sys.path.append("./mltools/libsvm-3.20/python")
import svmutil as libsvm

if len(sys.argv) != 4:
    print("Usage: python server.py [model-file] [range-file] [port-number]")
    exit(0)

model = libsvm.svm_load_model(sys.argv[1])
util.load_bound(sys.argv[2])

class Media:
   def __init__(self, media, l=""):
      self.url = media["images"]["low_resolution"]["url"]
      self.user = media["user"]["username"]
      self.post = media["caption"]["text"] if media["caption"] else ""
      self.post = self.post[:100]
      self.label = l

class AjaxHandler(tornado.web.RequestHandler):
   def get(self, tag, max_tag_id):
      #print tag
      p = Pool(10)

      medias, next_ = util.search_by_tag(tag, 3, max_tag_id)

      fs = p.map(util.features, medias)

      p_label, _, _ = libsvm.svm_predict([1] * len(fs), fs, model, "-q")
      medias = map(lambda (m, l): Media(m, l).__dict__, zip(medias, p_label))

      self.write(json.dumps({
         "max_tag_id": next_,
         "medias": medias
       }))
      
      p.close()
      p.join()

class MainHandler(tornado.web.RequestHandler):
   def initialize(self, prefix=None):
      self.prefix = prefix

   def get(self, tag="貓咪", max_tag_id=None):
      if tag == "":
         tag = "貓咪"
      p = Pool(10)

      if self.prefix == "ajax":
         medias, next_ = util.search_by_tag(tag, 3, max_tag_id)
      else:
         medias, next_ = util.search_by_tag(tag, 5, max_tag_id)

      fs = p.map(util.features, medias)
      p_label, _, _ = libsvm.svm_predict([1] * len(fs), fs, model)
      #for (m, f) in zip(medias, fs):
         #print(m["caption"]["text"])
         #print(f)
      if self.prefix == "ajax":
         medias = map(lambda (m, l): Media(m, l).__dict__, zip(medias, p_label))
         self.write(json.dumps({
            "max_tag_id": next_,
            "medias": medias
         }))
      else:
         medias = map(lambda (m, l): Media(m, l), zip(medias, p_label))
         if self.prefix == "demo1":
            self.render("demo1.html", medias=medias, tag_name=tag, max_tag_id=next_)
         elif self.prefix == "demo2":
            self.render("demo2.html", medias=medias, tag_name=tag, max_tag_id=next_)
         else:
            self.render("main.html", medias=medias, tag_name=tag, max_tag_id=next_)

      p.close()
      p.join()
      
application = tornado.web.Application([
      (r"/ajax/(.+)/(.+)", MainHandler, dict(prefix="ajax")),
      (r"/demo1/(.*)", MainHandler, dict(prefix="demo1")),
      (r"/demo2/(.*)", MainHandler, dict(prefix="demo2")),
      (r"/(.*)", MainHandler),
   ],
   template_path=os.path.join(os.path.dirname(__file__), "template")
)

if __name__ == "__main__":
   application.listen(int(sys.argv[3]))
   tornado.ioloop.IOLoop.instance().start()
