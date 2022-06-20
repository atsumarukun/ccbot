import asyncio
import aiohttp

async def ws_run_forever(session: aiohttp.ClientSession, model, chart) -> None:
    async with session.ws_connect(model.WEBSOCKET_URL) as ws:
        await ws.send_json(model.params)
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                try:
                    model.orderbook(msg.json())
                    await chart.draw_chart()
                except:
                    pass
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print(msg.json())
                quit()
