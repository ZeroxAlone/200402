# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:24:48 2020

@author: lisa_
"""


import websockets
import asyncio

cs = set()

async def talk(websocket, path):
    try:
        while True:
            if (not websocket in cs):
                cs.add(websocket)
                msg="Welcome: "+str(websocket.remote_address)
            else:
                msg = str(websocket.remote_address)+"said: "+str(await websocket.recv())
            await asyncio.wait([ws.send(msg) for ws in cs])
    except Exception as err:
        cs.remove(websocket)

start_server = websockets.serve(talk, "locoalhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
