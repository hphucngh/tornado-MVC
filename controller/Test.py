from . import BaseController, DBConnection
import torndb

import tornado.escape
import tornado.ioloop
import tornado.web


class Test(BaseController):
    def get(self):
        conn = DBConnection.DBConnection
        rows = conn.query("select Id,Title from post")
        conn.close()

        top = "<html><body><b>Posts</b><br /><br />"
        table = "<table border=\"1\"><col width=\"50\" /><col width=\"200\" />"
        for row in rows:
            table += "<tr><td>" + str(row["Id"]) + "</td><td>" + str(row["Title"]) + "</td></tr>"
        bottom = "</body></html>"
        self.write(top+table+bottom) 
