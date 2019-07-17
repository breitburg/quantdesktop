from . import BaseModule

from logging import info
from requests import post
from time import time

from pynput.mouse import Controller
mouse = Controller()


class MouseModule(BaseModule):
    def __init__(self):
        super().__init__(name='mouse')

    def update(self):
        values = mouse.position
        try:
            post(
                'http://192.168.0.3:5000/data',
                json={'id': 0, 'source': 100, 'value': [{'time': time(), 'x': values[0], 'y': values[1]}]})
            info(f'Отправлены данные: {values}')
        except Exception as exception:
            info(f'Возникла проблема при подключению: {exception}')
