from . import BaseModule

from time import time, sleep
from threading import Thread

# Создаем контроллер мыши
from pynput.mouse import Controller
mouse = Controller()


class MouseModule(BaseModule):
    move_events = list()

    def __init__(self):
        super().__init__(name='mouse', source=100)

        # Создаем поток для трекинга передвижений мыши
        # передаем в функцию массив передвижений
        clicks_thread = Thread(target=move_event, args=(self.events, ))
        clicks_thread.start()


def move_event(key_events):
    while True:
        values = mouse.position

        # Если данные такие-же добавляем только один блок данных
        if (len(key_events) > 0 and key_events[-1]['x'] != values[0] and key_events[-1]['y'] != values[1]) or len(key_events) == 0:
            key_events.append(dict(x=values[0], y=values[1], time=time()))
        sleep(1)