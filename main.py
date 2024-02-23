import pprint
import tkinter as tk
import logging
from connectors.binance_futures import BinanceFuturesClient
from dotenv import load_dotenv
import os

load_dotenv()
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

    pprint.pprint(binance.get_historical_candles("BTCUSDT", "1h"))

    root = tk.Tk()
    root.mainloop()

