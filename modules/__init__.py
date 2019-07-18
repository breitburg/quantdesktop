class BaseModule:
    """Материнский класс для написания модулей"""
    url = 'http://192.168.0.3:5000/data'  # URL для отправки данных

    def __init__(self, name):
        self.name = name

    def update(self):
        # Метод который выполняет функцию получения,
        # форматирования и отправки данных на сервер
        pass


# Импорт модулей
from .mouse import MouseModule  # Мышь
from .keyboard import KeyboardModule  # Клавиатура

# Массив модулей для запуска
to_load = [
    MouseModule(),  # Инициализируем модуль мыши
    KeyboardModule()  # Инициализируем модуль клавиатуры
]
