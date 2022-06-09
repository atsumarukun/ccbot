import asyncio
import aiohttp

from ccbot.ws import ws_run_forever
from ccbot.models.bitflyer import Bitflyer

async def main():
    bitflyer = Bitflyer("BTC_JPY")

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            ws_run_forever(session, bitflyer)
        )

if __name__ == "__main__":
    asyncio.run(main())
