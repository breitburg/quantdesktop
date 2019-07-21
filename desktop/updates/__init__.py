from os import getcwd
from platform import system
from logging import critical
from logging import info
from webbrowser import open as openurl
from desktop.uis import messagebox
from requests import get

info('Отправка запроса')
release = get('https://api.github.com/repos/breitburg/quantify-desktop/releases/latest').json()
info('Готово!')
path = getcwd()


def check_new():
    from desktop.config import __version__
    return release['tag_name'] != __version__


def check_updates():
    while True:
        if not check_new(): break
        info(f'Обновление! ({release.tag_name})')
        assets = release['assets']
        url = assets[0]['browser_download_url']

        result = messagebox.askquestion('Обновление', f'Доступна новая версия ({release["tag_name"]})!\n'
        f'Хотите скачать обновление?', icon='warning')
        if result == 'yes':
            openurl(url=url)
            quit()
