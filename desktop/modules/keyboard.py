from threading import Thread
from pynput.keyboard import Listener
from time import time
from . import BaseModule


class KeyboardModule(BaseModule):
    def __init__(self):
        super().__init__(name='keyboard', source=101)

        # Создаем поток для трекинга нажатий на клавиатуру
        # передаем в функцию массив нажатых клавиш
        keys_thread = Thread(target=key_tracking, args=(self.events, ))
        keys_thread.start()

    def update(self):
        return self.events


def key_tracking(key_events):
    # Метод обрабатывающий нажатие клавиш
    # при получении события нажатия на кнопку добавляем данные в массив
    with Listener(on_press=lambda key: key_events.append(dict(time=time(), button=str(key) if str(key).endswith('\'') and str(key).startswith('\'') else f'\'{str(key)}\''))) as listener:
        listener.join()
