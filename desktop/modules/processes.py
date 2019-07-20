from . import BaseModule
from psutil import process_iter
from time import time

# Создаем контроллер мыши
from pynput.mouse import Controller
mouse = Controller()


class ProcessesModule(BaseModule):
    def __init__(self):
        super().__init__(name='processes', source=102)

    def update(self):
        for proc in process_iter():
            block = proc.as_dict(attrs=['name', 'create_time'])
            block['time'] = time()
            self.events.append(block)
        return self.events