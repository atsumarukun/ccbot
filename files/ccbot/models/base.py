from sortedcontainers import SortedDict

class ModelBase:
    def __init__(self):
        self.asks = SortedDict()
        self.bids = SortedDict()

    def orderbook(self) -> dict:
        pass

    def _update(self, ob: SortedDict, data: list, sign: int) -> None:
        for d in data:
            p, s = float(d["price"]), float(d["size"])
            if s == 0:
                ob.pop(p * sign, None)
            else:
                ob[p * sign] = [p, s]
