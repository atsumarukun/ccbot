import asyncio
import aiohttp

async def ws_run_forever(session: aiohttp.ClientSession, chart) -> None:
    async with session.ws_connect(chart.c.WEBSOCKET_URL) as ws:
        await ws.send_json(chart.c.params)
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                chart.c.orderbook(msg.json())
                await chart.draw_chart()
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print(msg.json())
                quit()
