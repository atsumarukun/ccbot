from sortedcontainers import SortedDict

from ccbot.models.base import ModelBase

class Coincheck(ModelBase):
    WEBSOCKET_URL = "wss://ws-api.coincheck.com/"

    def __init__(self, symbol):
        super().__init__()
        self.params = {"type": "subscribe", "channel": f"{symbol}-orderbook"}

    def orderbook(self, msg: dict) -> dict:
        self._update(self.asks, msg[1]["asks"], 1)
        self._update(self.bids, msg[1]["bids"], -1)
        return {"asks": self.asks, "bids": self.bids}

    def _update(self, ob: SortedDict, data: list, sign: int) -> None:
        for d in data:
            p, s = float(d[0]), float(d[1])
            if s == 0:
                ob.pop(p * sign, None)
            else:
                ob[p * sign] = [p, s]
