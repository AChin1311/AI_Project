#-*- encoding: utf-8 -*-
import tornado.ioloop
import tornado.web
import util
from multiprocessing import Pool

class MainHandler(tornado.web.RequestHandler):
   def get(self, tag):
      if tag == "":
         return
      medias = util.search_by_tag(tag, 5)

      p = Pool(5)
      p.map(util.features, medias)
      for media in medias:
         self.write("<img src=%s />" % media["images"]["low_resolution"]["url"])
         self.flush()

application = tornado.web.Application([
   (r"/(.*)", MainHandler),
])

if __name__ == "__main__":
   application.listen(8888)
   tornado.ioloop.IOLoop.instance().start()
