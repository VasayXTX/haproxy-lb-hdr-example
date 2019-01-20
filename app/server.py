import os
import socket

from aiohttp import web


async def hello_handle(request: web.Request):
    text = "Hello from {}".format(socket.gethostname())
    return web.Response(text=text)


if __name__ == '__main__':
    app = web.Application()
    app.add_routes([web.get('/', hello_handle)])
    web.run_app(app, port=int(os.environ.get('PORT', '8080')))
