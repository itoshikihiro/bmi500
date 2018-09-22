import json
import tornado.ioloop
import tornado.web


with open('distros.json', 'r') as f:
    distros_dict = json.load(f)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        distros = {}
        distro_str = ''
        i = 0
        
        o_id = self.get_arguments("oid")

        if o_id == []:
            self.set_status(400)
            return self.finish("Invalid distribution id")
        
        for distro in distros_dict:
            
            if distro['Name'].lower() == o_id[0].lower():
                distros[i] = distro
                i = i + 1

        distro_str = json.dumps(distros, indent=4)        

        self.write(distros)


# localhost:8888?oid=debian

def make_app():

    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    print('Listening on port 8888')
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
