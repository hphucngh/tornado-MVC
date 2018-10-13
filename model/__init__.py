import tornado.web
from controller import Hello, VersionHandler, Test
from config import Env

class router:
    def __init__(self):
        self.router = tornado.web.Application([
            (r'/hello', Hello),
            (r"/version", VersionHandler),
            (r"/test", Test)
        ])

        self.router.listen(Env.PORT)

