import asyncio
import aiohttp

from ccbot.ws import ws_run_forever
from ccbot.models.gmocoin import Gmocoin
from ccbot.models.bitflyer import Bitflyer
from ccbot.models.coincheck import Coincheck
from ccbot.models.liquid import Liquid
from ccbot.chart import Chart

async def main():
    gmocoin = Gmocoin("BTC_JPY")
    bitflyer = Bitflyer("BTC_JPY")
    coincheck = Coincheck("btc_jpy")
    liquid = Liquid("btcjpy")
    chart = Chart(gmocoin, bitflyer, coincheck, liquid)

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            ws_run_forever(session, gmocoin, chart),
            ws_run_forever(session, bitflyer, chart),
            ws_run_forever(session, coincheck, chart),
            ws_run_forever(session, liquid, chart)
        )

if __name__ == "__main__":
    asyncio.run(main())
