import tornado
import tornado.web
import tornado.ioloop

#program to test bokeh plot as a tornado web application
#I wasn't sure if he wanted this or not, I tried hosting it with my UMD webpage but was running into problems
#test at localhost:80/languagemap in your browser after running


#request handler for html files
class myRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("final.html")

#main application web app
if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/languagemap", myRequestHandler)
    ])

#listenn on port 80
app.listen(80)
tornado.ioloop.IOLoop.current().start()
