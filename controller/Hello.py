from . import BaseController

class Hello(BaseController):
    def get(self):
        self.write('Hello MVC')