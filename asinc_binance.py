import matplotlib.pyplot as plt
import websockets
import asyncio
import json
import time


xdata = []
ydata = []

fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

def update_graph():
    ax.plot(xdata, ydata, color='g')
    ax.legend([f"Last price: {ydata[-1]}$"])

    fig.canvas.draw()
    plt.pause(2)

async def main():
    url = "wss://stream.binance.com:9443/stream?streams=btcusdt@miniTicker"
    async with websockets.connect(url) as client:
        while True:
            data = json.loads(await client.recv())["data"]

            #Наносекунды (data["E"]) перевести в localtime-(обычные секунды)
            event_time = time.localtime(data["E"] // 1000)
            event_time = f"{event_time.tm_hour}:{event_time.tm_min}:{event_time.tm_sec}"

            print(event_time, "->", data["c"])

            xdata.append(event_time)
            ydata.append(data["c"][0:5])
            update_graph()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
