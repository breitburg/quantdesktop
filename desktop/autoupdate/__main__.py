from os.path import join, abspath
from os import getcwd
from platform import system
from logging import critical

if system() == 'Windows':
    critical(f'{system()} не поддерживает автообновление.\n'
             f'Для автообновления рекомендуем использовать PyPi:\n'
             f'pip install --upgrade quantify-desktop')

    # Бывает что input выполняется быстрее чем вывод сообщения
    from time import sleep
    sleep(0.1)  # :)

    input('Press any key...')
    quit(0)

path = getcwd()

from setup import __version__
from requests import get
print(get('https://gitlab.com/api/v4/projects/13353621/releases').json())