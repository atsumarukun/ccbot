from ccbot.methods.base import MethodBase

class Test:
    def __init__(self, *args):
        super().__init__()
        self.coms = args

    async def main(self):
        max_com, min_com = self.coms[0], self.coms[0]
        for com in self.coms[1:]:
            if com.asks.values()[0][0] > max_com.asks.values()[0][0]:
                max_com = com
            elif com.asks.values()[0][0] < min_com.asks.values()[0][0]:
                min_com = com
        ask_diff = max_com.asks.values()[0][0] - min_com.asks.values()[0][0]
        bid_diff = max_com.asks.values()[1][0] - min_com.asks.values()[1][0]

        print(type(max_com).__name__, type(min_com).__name__, ask_diff, bid_diff)
