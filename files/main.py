import asyncio
import aiohttp

from ccbot.ws import ws_run_forever
from ccbot.models.coincheck import Coincheck
from ccbot.chart import Chart

async def main():
    coincheck = Coincheck("btc_jpy")
    chart = Chart(coincheck)

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            ws_run_forever(session, chart)
        )

if __name__ == "__main__":
    asyncio.run(main())
