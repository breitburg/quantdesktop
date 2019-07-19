from . import BaseModule

from logging import info
from requests import post
from time import time, sleep
from threading import Thread

# Создаем контроллер мыши
from pynput.mouse import Controller
mouse = Controller()


class MouseModule(BaseModule):
    move_events = list()

    def __init__(self):
        super().__init__(name='mouse')

        # Создаем поток для трекинга передвижений мыши
        # передаем в функцию массив передвижений
        clicks_thread = Thread(target=move_event, args=(self.move_events, ))
        clicks_thread.start()

    def update(self):
        # Метод получения и отправки данных на сервер
        try:
            post(self.url, json=dict(id_device=0, source=100, value=self.move_events))
            info(f'Отправлены данные: {self.move_events}')
            self.move_events.clear()
        except Exception as exception:
            info(f'Возникла проблема при подключению: {exception}')


def move_event(key_events):
    while True:
        values = mouse.position
        key_events.append(dict(x=values[0], y=values[1], time=time()))
        sleep(2)