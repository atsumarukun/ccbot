from sortedcontainers import SortedDict

from ccbot.models.base import ModelBase

class Binance(ModelBase):
    WEBSOCKET_URL = "wss://stream.binance.com:9443/ws"

    def __init__(self, symbol: str):
        super().__init__()
        self.params = {"method": "SUBSCRIBE", "params": [f"{symbol}@depth"], "id": 1}

    def orderbook(self, msg: dict) -> dict:
        self._update(self.asks, msg["a"], 1)
        self._update(self.bids, msg["b"], -1)
        return {"asks": self.asks, "bids": self.bids}


    def _update(self, ob: SortedDict, data: list, sign: int) -> None:
        for d in data:
            p, s = float(d[0]), float(d[1])
            if s == 0:
                ob.pop(s * sign, None)
            ob[p * sign] = [p, s]
