import tornado.web
import torndb
from config import Env

class DBConnection:
    DBConnection = torndb.Connection(
            host= Env.DB_HOST, 
            database= Env.DB_NAME,
            user= Env.DB_USER,
            password= Env.DB_PASSWORD
        )

class BaseController(tornado.web.RequestHandler):
    def render (self, tpl, **render_data):
        if not tpl.endswith('html'):
            tpl = "{}.html".format(tpl)
        super().render(tpl, **render_data)

class My404(BaseController):
    def get(self):
        self.render("404")

from .Hello import Hello
from .VersionHandler import VersionHandler
from .Test import Test
__all__ ={
            ("Hello", "My404"),
            ("VersionHandler", "My404"),
            ("Test", "My404")
        }


