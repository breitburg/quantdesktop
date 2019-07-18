from pystray import Icon, Menu, MenuItem
from config import config
from PIL import Image
from platform import system


def on_clicked(icon, item):
    # Обработка нажатия на чекбокс
    title = 'mouse' if item.text == 'Мышь' else 'keyboard'
    config.set_value(title, not config.get_value(title))  # Ставим значение в конфиге


# Создаем инстанс приложения
app = Icon('Quantify', Image.open('assets/icon_win.png' if system() == 'Darwin' else '../assets/icon_win.png'), menu=Menu(
        MenuItem(text='Мышь', action=on_clicked, checked=lambda x: config.get_value('mouse')),
        MenuItem(text='Клавиатура', action=on_clicked, checked=lambda x: config.get_value('keyboard'))
    ))
