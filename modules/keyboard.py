from threading import Thread
from pynput.keyboard import Listener
from time import time, sleep
from . import BaseModule


class KeyboardModule(BaseModule):
    key_events = []

    def __init__(self):
        super().__init__(name='keyboard')
        keys_thread = Thread(target=self.key_tracking, args=(self.key_events, ))
        keys_thread.start()

    @staticmethod
    def key_tracking(key_events):
        with Listener(on_press=lambda key: key_events.append({'time': time(), 'button': key})) as listener:
            listener.join()

    def update(self):
        print('Мы нажали ' + str(len(self.key_events)) + ' клавиш')
        self.key_events.clear()
