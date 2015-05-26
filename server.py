#-*- encoding: utf-8 -*-
import sys
import tornado.ioloop
import tornado.web
import util
from multiprocessing import Pool
sys.path.append("./liblinear-1.96/python")
import liblinearutil as liblr

m = liblr.load_model("./10.model")

class MainHandler(tornado.web.RequestHandler):
   def get(self, tag):
      p = Pool(10)
      if tag == "":
         return
      media_gen = util.search_by_tag(tag, 5)
      for _ in range(0, 10):
         medias = media_gen.next()

         fs = p.map(util.features, medias)

         p_label, _, _ = liblr.predict([], fs, m)
         for x in zip(p_label, fs):
            print x
         for (label, (f, media)) in zip(p_label, zip(fs, medias)):
            self.write("<img src=%s />%s %s %d<br>" % (media["images"]["low_resolution"]["url"], media["caption"]["text"], str(f), label))
            self.flush()
      p.close()
      p.join()

application = tornado.web.Application([
   (r"/(.*)", MainHandler),
])

if __name__ == "__main__":
   application.listen(8888)
   tornado.ioloop.IOLoop.instance().start()
