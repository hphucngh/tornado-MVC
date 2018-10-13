import tornado.ioloop
from model import *

def main():
    model = router()
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()

