import signal
import tkinter
from logging import info
from platform import system

from PIL import Image
from pystray import Icon, Menu, MenuItem
from requests import get

from desktop.config import config
from desktop.uis import messagebox


def on_clicked(icon, item):
    # Обработка нажатия на чекбокс
    title = 'mouse' if item.text == 'Мышь' else 'keyboard' if item.text == 'Клавиатура' else 'processes'
    config.set_value(title, not config.get_value(title))  # Ставим значение в конфиге


def get_auth_code(icon, item):
    from ..config import url_endpoint
    from ..extras.id import generate_id
    from platform import uname
    info('Отправка запроса')
    try:
        responce = get(f'{url_endpoint}2fa?id_device={generate_id()}&name={uname().node}').json()
        info('Код получен')
    except Exception as ex:
        messagebox.showinfo('Просмотр кода', f'Сервер не доступен.')
        return

    root = tkinter.Tk()
    messagebox.showinfo('Просмотр кода', f'Ваш код: {responce["code"]}\n'
    f'Код остается валидным только 10 минут.', master=root)
    root.destroy()

    info('Ответ!')
    signal.signal(signal.SIGKILL, signal.SIG_DFL)


# Создаем инстанс приложения
from os.path import join, abspath
from os import getcwd

app = Icon('Quantify', Image.open(
    join(getcwd() if system() == 'Windows' else abspath(__file__).replace(join('uis', 'universal.py'), ''), 'assets',
         'toolbar_icon.png')), menu=Menu(
    MenuItem(text='Мышь', action=on_clicked, checked=lambda x: config.get_value('mouse')),
    MenuItem(text='Клавиатура', action=on_clicked,
             checked=lambda x: config.get_value('keyboard') if system() != 'Darwin' else False,
             enabled=system() != 'Darwin'),
    MenuItem(text='Процессы', action=on_clicked, checked=lambda x: config.get_value('processes')),
    MenuItem(text='Другое', action=Menu(
        MenuItem(text='Получить код 2FA', action=get_auth_code)
    ))
))
