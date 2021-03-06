from ccbot.models.base import ModelBase

class Gmocoin(ModelBase):
    WEBSOCKET_URL = "wss://api.coin.z.com/ws/public/v1"

    def __init__(self, symbol: str):
        super().__init__()
        self.params = {"command": "subscribe", "channel": "orderbooks", "symbol": symbol}

    def orderbook(self, msg: dict) -> dict:
        self.asks.clear(), self.bids.clear()
        self._update(self.asks, msg["asks"], 1)
        self._update(self.bids, msg["bids"], -1)
        return {"asks": self.asks, "bids": self.bids}
