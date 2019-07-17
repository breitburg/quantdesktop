from platform import system
from threading import Thread
from time import sleep
from config import config


def puller():
    from modules import to_load
    from requests import get

    global is_alive
    is_alive = True

    while is_alive:
        for item in to_load:
            if config.get(item.name):
                values = item.update()
                get('http://httpbin.org/get')
                print(values)
            sleep(1)


puller_thread = Thread(target=puller, args=())
puller_thread.start()

if system() == 'Darwin':
    print('У нас мак')
    from uis.mac import app
    app.run()
    is_alive = False
else:
    print('У нас непонятная система')
    from uis.windows import run
    run()
    is_alive = False
