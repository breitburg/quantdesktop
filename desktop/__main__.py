from platform import system
from threading import Thread
from time import sleep
from desktop.config import config
from requests import post
from desktop.config import url_endpoint
from desktop.extras.id import generate_id
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
                value = item.update()  # вызываем update
                info(f'Собрано {len(value)} блоков данных!')
                try:
                    ready_to_send = value.copy()

                    limit = 50
                    if len(ready_to_send) > limit:
                        ready_to_send = ready_to_send[:limit]
                        del item.events[:50]
                    post(f'{url_endpoint}data', json=dict(id_device=generate_id(), source=item.source, value=ready_to_send))

                    info(f'Отправлены данные ({len(ready_to_send)}): {ready_to_send}')
                    item.events.clear()
                except Exception as exception:
                    info(f'Возникла проблема при подключению: {exception}')
        info('Ожидание...')
        sleep(10)


if __name__ == '__main__':

    # Пока переменная is_alive ровно True,
    # модули будут отправлять данные на сервер
    # в отдельном потоке
    is_alive = True

    if system() == 'Windows':
        info('Проверка обновлений...')
        from desktop.updates import check_updates
        check_updates()

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
