import matplotlib.pyplot as plt

class Chart:
    def __init__(self, *args):
        self.fig, self.ax = plt.subplots()
        self.fig.canvas.draw()
        self.bg = self.fig.canvas.copy_from_bbox(self.ax.bbox)

        self.coms = args

        for com in self.coms:
            com.top_asks = [0 for _ in range(100)]
            com.line, = self.ax.plot(com.top_asks)
        self.fig.show()

    async def draw_chart(self):
        self.fig.canvas.restore_region(self.bg)
        all_top_asks = []
        for com in self.coms:
            com.top_asks.append(com.asks.values()[0][0])
            del com.top_asks[0]
            com.line.set_ydata(com.top_asks)
            self.ax.draw_artist(com.line)
            all_top_asks += com.top_asks
        self.ax.set_ylim(min(all_top_asks), max(all_top_asks))
       
        self.fig.canvas.blit(self.ax.bbox)
        self.fig.canvas.flush_events()
