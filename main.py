import tkinter as tk
import logging
from bitmex_futures import get_contracts

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
    bitmex_contracts = get_contracts()

    root = tk.Tk()
    root.configure(bg="gray12")

    i = 0
    j = 0

    calibri_font = ("Calibri", 11, "normal")

    for contract in bitmex_contracts:
        label_widget = tk.Label(root, text=contract, bg='gray12', fg='SteelBlue1', width=13, font=calibri_font)
        label_widget.grid(row=i, column=j, sticky="ew")

        if i == 4:
            j += 1
            i = 0

        i += 1

    root.mainloop()

