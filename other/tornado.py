import asyncio
import tornado

class MainHandler(tornado.web.RequesHandler):
    def get(self):
        self.write("Hello, World")

def make_app():
    return tornado.web.Application([(r"/", MainHandler), ])

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
