import matplotlib.pyplot as plt

class Chart:
    def __init__(self, c):
        self.c = c
        self.asks = c.asks
        self.fig, self.ax = plt.subplots()
        self.fig.canvas.draw()
        self.bg = self.fig.canvas.copy_from_bbox(self.ax.bbox)
        self.data = [0 for _ in range(100)]
        self.line, = self.ax.plot(self.data)
        self.fig.show()

    async def draw_chart(self):
        self.data.append(self.asks.values()[0][0])
        del self.data[0]
        print(len(self.data))
        self.line.set_ydata(self.data)
        self.fig.canvas.restore_region(self.bg)
        self.ax.draw_artist(self.line)
        self.fig.canvas.blit(self.ax.bbox)
        self.fig.canvas.flush_events()
