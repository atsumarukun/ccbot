import asyncio
import aiohttp

from ccbot.ws import ws_run_forever
from ccbot.models.gmocoin import Gmocoin

async def main():
    gmocoin = Gmocoin("BTC_JPY")

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            ws_run_forever(session, gmocoin)
        )

if __name__ == "__main__":
    asyncio.run(main())
