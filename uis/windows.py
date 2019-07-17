from pystray import Icon, Menu, MenuItem
from config import config
from PIL import Image
from platform import system


def on_clicked(icon, item):
    title = 'mouse' if item.text == 'Мышь' else 'keyboard'
    config.set_value(title, not config.get(title))


def run():
    Icon('Quantify', Image.open('assets/icon_win.png' if system() == 'Darwin' else '../assets/icon_win.png'), menu=Menu(
        MenuItem(text='Мышь', action=on_clicked, checked=lambda x: config.get('mouse')),
        MenuItem(text='Клавиатура', action=on_clicked, checked=lambda x: config.get('keyboard'))
    )).run()
