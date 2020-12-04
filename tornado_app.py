# Langvis: A visualizer for world languages' locations.

# Copyright (C) 2020 Quinn Luetzow,  Angelique Bernik, Dakota Bond,
# Joseph Marchetti, Josh Kizilos.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""A Tornado application to display the Bokeh plot."""


import tornado
import tornado.web
import tornado.ioloop


#request handler for html files
class MyRequestHandler(tornado.web.RequestHandler):
    """Tornado custum handler."""
    def get(self):
        self.render("final.html")


#main application web app
if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/languagemap", MyRequestHandler)
    ])

    #listen on port 80
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
