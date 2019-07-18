from . import BaseModule

from logging import info
from requests import post
from time import time

# Создаем контроллер мыши
from pynput.mouse import Controller
mouse = Controller()


class MouseModule(BaseModule):
    def __init__(self):
        super().__init__(name='mouse')
        # TODO: Отдельный поток для получения событий нажатия

    def update(self):
        # Метод получения и отправки данных на сервер
        values = mouse.position
        try:
            post(self.url, json={'id': 0, 'source': 100, 'value': [{'time': time(), 'x': values[0], 'y': values[1]}]})
            info(f'Отправлены данные: {values}')
        except Exception as exception:
            info(f'Возникла проблема при подключению: {exception}')
