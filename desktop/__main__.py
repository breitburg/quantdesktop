from platform import system
from threading import Thread
from time import sleep
from desktop.config import config

from logging import info, basicConfig, INFO

# Установка уровня сообщений при котором
# они будут отображаться к консоли
basicConfig(level=INFO)


def server_pull(is_alive, to_load):
    # Параллельно с основным потоком вызываем
    # функцию update() у каждого модуля если пользователь
    # разрешил считывание данных с этого модуля

    while is_alive:
        info('Новая итерация цикла...')
        for item in to_load:
            if config.get_value(item.name):
                info(f'Обновляем данные для {item.name}')
                item.update()  # вызываем update
        info('Ожидание...')
        sleep(10)


if __name__ == '__main__':

    # Пока переменная is_alive ровно True,
    # модули будут отправлять данные на сервер
    # в отдельном потоке
    is_alive = True

    # Поток для фоновой обновления и отправки данных
    # модулей на сервер
    from desktop.modules import to_load
    puller_thread = Thread(target=server_pull, args=(is_alive, to_load, ))
    puller_thread.start()  # Запуск потока

    # Получаем тип текущей системы
    system_type = system()
    info(f'Запущено на {system_type}')

    # В зависимости от системы запускаем разные
    # реализации тулбар меню
    from desktop.uis.universal import app
    app.run()

    # После завершения работы тулбар
    # меню завершаем поток обновления модулей
    is_alive = False
