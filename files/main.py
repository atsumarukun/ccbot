import asyncio
import aiohttp

from ccbot.ws import ws_run_forever
from ccbot.models.gmocoin import Gmocoin
from ccbot.models.bitflyer import Bitflyer
from ccbot.models.coincheck import Coincheck
from ccbot.models.liquid import Liquid
from ccbot.chart import Chart
from ccbot.methods.test import Test

async def main():
    gmocoin = Gmocoin("BTC_JPY")
    bitflyer = Bitflyer("BTC_JPY")
    coincheck = Coincheck("btc_jpy")
    liquid = Liquid("btcjpy")
    #chart = Chart(gmocoin, bitflyer, coincheck, liquid)
    test = Test(gmocoin, bitflyer, coincheck, liquid)

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            ws_run_forever(session, gmocoin, test),
            ws_run_forever(session, bitflyer, test),
            ws_run_forever(session, coincheck, test),
            ws_run_forever(session, liquid, test)
        )

if __name__ == "__main__":
    asyncio.run(main())
