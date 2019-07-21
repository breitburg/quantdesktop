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
            block = proc.as_dict(attrs=['name', 'memory_percent', 'username', 'create_time'])
            if type(block['memory_percent']) != float: continue
            block['time'] = time()
            block['username'] = '' if block['username'] == None else block['username']
            self.events.append(block)
        self.events = sorted(self.events, key=lambda i: i['memory_percent'])
        return self.events[-50:]
