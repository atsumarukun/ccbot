import asyncio
import aiohttp

from ccbot.exception import TimeOutException

async def ws_run_forever(session: aiohttp.ClientSession, model, function) -> None:
    async with session.ws_connect(model.WEBSOCKET_URL) as ws:
        await ws.send_json(model.params)
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                try:
                    model.orderbook(msg.json())
                    # await function.main()
                except TimeOutException as e:
                    print(f"[{type(model).__name__}] Reconnect websocket.")
                    model.params["event"] = "pusher:unsubscribe"
                    await ws.send_json(model.params)
                    await asyncio.sleep(3)
                    model.params["event"] = "pusher:subscribe"
                    await ws.send_json(model.params)
                    model.i = 0
                except (TypeError, KeyError):
                    pass
                except:
                    import traceback
                    traceback.print_exc()
                    quit()
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print(msg.json())
                quit()
