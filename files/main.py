import asyncio
import aiohttp

from ccbot.ws import ws_run_forever
from ccbot.models.coincheck import Coincheck

async def main():
    coincheck = Coincheck("btc_jpy")

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            ws_run_forever(session, coincheck)
        )

if __name__ == "__main__":
    asyncio.run(main())
