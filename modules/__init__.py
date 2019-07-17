class BaseModule:
    url = 'http://192.168.0.3:5000/data'

    def __init__(self, name):
        self.name = name

    def update(self):
        pass


# Импорт модулей
from .mouse import MouseModule
from .keyboard import KeyboardModule

to_load = [
    MouseModule(),
    KeyboardModule()
]
