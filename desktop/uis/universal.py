from pystray import Icon, Menu, MenuItem
from desktop.config import config
from PIL import Image
from platform import system

def on_clicked(icon, item):
    # Обработка нажатия на чекбокс
    title = 'mouse' if item.text == 'Мышь' else 'keyboard'
    config.set_value(title, not config.get_value(title))  # Ставим значение в конфиге


# Создаем инстанс приложения
from os.path import join, abspath
from os import getcwd
app = Icon('Quantify', Image.open(
    join(getcwd() if system() == 'Windows' else abspath(__file__).replace(join('uis', 'universal.py'), ''), 'assets', 'toolbar_icon.png')), menu=Menu(
        MenuItem(text='Мышь', action=on_clicked, checked=lambda x: config.get_value('mouse')),
        MenuItem(text='Клавиатура', action=on_clicked, checked=lambda x: config.get_value('keyboard'))
    ))