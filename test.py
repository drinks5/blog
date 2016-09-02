# -*- coding: utf-8 -*-
# @Author: drinks
# @Date:   2016-05-27 21:29:54
# @Last Modified by:   drinks
# @Last Modified time: 2016-06-10 21:41:50
from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(body=text.encode('utf-8'))

async def wshandler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.tp == web.MsgType.text:
            ws.send_str("Hello, {}".format(msg.data))
        elif msg.tp == web.MsgType.binary:
            ws.send_bytes(msg.data)
        elif msg.tp == web.MsgType.close:
            break

    return ws


app = web.Application()
app.router.add_route('GET', '/echo', wshandler)
app.router.add_route('GET', '/{name}', handle)

web.run_app(app)
