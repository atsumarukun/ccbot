import json
from sortedcontainers import SortedDict

from ccbot.models.base import ModelBase

class Liquid(ModelBase):
    WEBSOCKET_URL = "wss://tap.liquid.com/app/LiquidTapClient"

    def __init__(self, symbol: str):
        super().__init__()
        self.params = {"event": "pusher:subscribe","data": {"channel": f"price_ladders_cash_{symbol}"}}

    def orderbook(self, msg: dict) -> dict:
        self.asks.clear(), self.bids.clear()
        self._update(self.asks, json.loads(msg["data"])["asks"], 1)
        self._update(self.bids, json.loads(msg["data"])["bids"], -1)
        return {"asks": self.asks, "bids": self.bids}

    def _update(self, ob: SortedDict, data: list, sign: int) -> None:
        for d in data:
            p, s = float(d[0]), float(d[1])
            ob[p * sign] = [p, s]
