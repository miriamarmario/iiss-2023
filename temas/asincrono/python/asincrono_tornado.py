import tornado.ioloop
import tornado.web
import time

class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        self.write("¡Bienvenido al mundo de Harry Potter!")
        await self.do_work()

    async def do_work(self):
        self.write("<br/>Iniciando la búsqueda del Horrocrux...")
        await self.search_horcrux()
        self.write("<br/>¡Horrocrux encontrado!")

    async def search_horcrux(self):
        self.write("<br/>Buscando en el Lago Negro...")
        await self.sleep()
        self.write("<br/>Buscando en la Cueva de las Maravillas...")
        await self.sleep()
        self.write("<br/>Buscando en el Bosque Prohibido...")
        await self.sleep()
        self.write("<br/>Buscando en el Valle de Godric...")
        await self.sleep()
        self.write("<br/>Buscando en el Callejón Diagon...")
        await self.sleep()
        self.write("<br/>Buscando en la Torre de Astronomía...")
        await self.sleep()
        self.write("<br/>Buscando en el Cementerio de Little Hangleton...")

    async def sleep(self):
        await tornado.ioloop.IOLoop.current().run_in_executor(None, time.sleep, 1)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
