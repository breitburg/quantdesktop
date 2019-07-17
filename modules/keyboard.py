from threading import Thread
from pynput.keyboard import Listener
from time import time, sleep
from . import BaseModule

key_events = []
class KeyboardModule(BaseModule):
    def __init__(self):
        super().__init__(name='keyboard')

    @staticmethod
    def key_tracking(key_events):
        with Listener(on_press=lambda key: key_events.append({'time': time(), 'button': key})) as listener:
            listener.join()

    def update(self):
        thread = Thread(target=self.key_tracking, args=(key_events, ))
        thread.start()

        print('Мы нажали ' + str(len(key_events)) + ' клавиш')
        key_events.clear()
