import asyncio
import aiohttp

async def ws_run_forever(session: aiohttp.ClientSession, model) -> None:
    async with session.ws_connect(model.WEBSOCKET_URL) as ws:
        await ws.send_json(model.params)
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                print(model.orderbook(msg.json()))
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print(msg.json())
                quit()
