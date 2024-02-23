import pprint
import tkinter as tk
import logging
from connectors.binance_futures import BinanceFuturesClient
from dotenv import load_dotenv
import os

load_dotenv("binance-keys.env")
public_key = os.getenv("PUBLIC_KEY")
secret_key = os.getenv("SECRET_KEY")

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)
streamHandler.setLevel(logging.INFO)

fileHandler = logging.FileHandler('info.log')
fileHandler.setFormatter(formatter)
fileHandler.setLevel(logging.DEBUG)

logger.addHandler(streamHandler)
logger.addHandler(fileHandler)


if __name__ == '__main__':
    binance = BinanceFuturesClient(public_key, secret_key, True)

    # print(binance.place_order("BTCUSDT", "BUY", 0.01, "LIMIT", 20000, "GTC"))
    print(binance.get_order_status("BTCUSDT", 3709320385))
    print(binance.cancel_order("BTCUSDT", 3709320385))

    root = tk.Tk()
    root.mainloop()

