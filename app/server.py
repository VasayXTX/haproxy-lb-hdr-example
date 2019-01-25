import os
import uuid
import socket

from aiohttp import web


async def hello_handle(request: web.Request):
    text = "Hello from {} !".format(socket.gethostname())
    resp = web.Response(text=text)
    if 'SESS_ID' not in request.cookies:
        sess_id = str(uuid.uuid4())
        resp.cookies['SESS_ID'] = sess_id
        print("new SESS_ID: {}".format(sess_id))
    return resp


if __name__ == '__main__':
    app = web.Application()
    app.add_routes([web.get('/', hello_handle)])
    web.run_app(app, port=int(os.environ.get('PORT', '8080')))
