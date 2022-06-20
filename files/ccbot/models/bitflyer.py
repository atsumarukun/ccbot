from ccbot.models.base import ModelBase

class Bitflyer(ModelBase):
    WEBSOCKET_URL="wss://ws.lightstream.bitflyer.com/json-rpc"

    def __init__(self, symbol: str):
        super().__init__()
        self.params = {"method": "subscribe", "params": {"channel": f"lightning_board_{symbol}"}}

    def orderbook(self, msg: dict) -> dict:
        self._update(self.asks, msg["params"]["message"]["asks"], 1)
        self._update(self.bids, msg["params"]["message"]["bids"], -1)
        return {"asks": self.asks, "bids": self.bids}
