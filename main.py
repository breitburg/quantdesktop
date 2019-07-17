from platform import system
from threading import Thread
from time import sleep
from config import config

from logging import info, basicConfig, INFO
basicConfig(level=INFO)


def server_pull(is_alive):
    from modules import to_load

    while is_alive:
        for item in to_load:
            if config.get(item.name):
                item.update()
            sleep(10)

is_alive = True
puller_thread = Thread(target=server_pull, args=(is_alive, ))
puller_thread.start()

system_type = system()
info(f'Запущено на {system_type}')

if system_type == 'Darwin':
    from uis.mac import app
    app.run()
else:
    from uis.windows import run
    run()
is_alive = False
