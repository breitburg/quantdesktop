from threading import Thread
from pynput.keyboard import Key, Listener
from time import time, sleep

key_events = []


def key_tracking():
    global key_events
    with Listener(on_press=lambda key: key_events.append({"time": time(), "button": key})) as listener:
        listener.join()


thread = Thread(target=key_tracking)
thread.start()

while True:
    print('Мы нажали ' + str(len(key_events)) + ' клавиш')
    key_events.clear()
    sleep(2)
