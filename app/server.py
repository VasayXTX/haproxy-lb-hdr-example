import logging
import os
import socket

from aiohttp import web


async def hello_handle(request: web.Request):
    session_id = request.headers.get('X-SESSION-ID')
    text = "[{}] Hello from {}!".format(session_id, socket.gethostname())
    resp = web.Response(text=text)
    return resp


async def healthz_handle(_: web.Request):
    resp = web.Response(text="OK")
    return resp


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = web.Application()
    app.add_routes([web.get('/hello', hello_handle)])
    app.add_routes([web.get('/healthz', healthz_handle)])
    web.run_app(app, port=int(os.environ.get('PORT', '8080')))
