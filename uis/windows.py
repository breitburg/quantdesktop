from pystray import Icon, Menu, MenuItem
from config import config
from PIL import Image


def on_clicked(item):
    title = 'mouse' if item.text == 'Мышь' else 'keyboard'
    config.set_value(title, not config.get(title))


def run():
    # TODO: Решить проблемы с отметками

    Icon('Quantify', Image.open('assets/icon_win.png'), menu=Menu(
        MenuItem('Мышь', on_clicked, checked=lambda x: config.get('mouse')),
        MenuItem('Клавиатура', on_clicked, checked=lambda x: config.get('keyboard'))
    )).run()
