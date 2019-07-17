from platform import system
from threading import Thread
from time import sleep
from config import config


def puller():
    from modules import to_load

    global is_alive
    is_alive = True

    while is_alive:
        for item in to_load:
            if config[item.name]: print(item.update())
            sleep(1)


puller_thread = Thread(target=puller, args=())
puller_thread.start()

if system() == 'Windows':
    print('У нас винда')
    is_alive = False
elif system() == 'Darwin':
    print('У нас мак')
    from uis.mac import app
    app.run()
    is_alive = False
else:
    print('Система не поддерживается')
    is_alive = False
