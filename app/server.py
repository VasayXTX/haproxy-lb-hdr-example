import os
import socket

from aiohttp import web


async def hello_handle(request: web.Request):
    session_id = request.headers.get('X-SESSION-ID')
    text = "[{}] Hello from {}!".format(session_id, socket.gethostname())
    resp = web.Response(text=text)
    return resp


if __name__ == '__main__':
    app = web.Application()
    app.add_routes([web.get('/', hello_handle)])
    web.run_app(app, port=int(os.environ.get('PORT', '8080')))
