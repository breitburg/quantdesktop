# desktop-client

![](http://g.recordit.co/1Cuc3QmjE9.gif)

Репозиторий содержащий приложение, которое отправляет данные о пользователе на сервер для анализа.

## Сборка

1. Установить `pyinstaller` и `pypiwin32`:
```console
pip install pyinstaller
pip install pypiwin32
```

2. Запустить сборку
```console
pyinstaller --noconsole --name "Desktop Client" --add-data "desktop\assets;assets" desktop\__main__.py
```

## Заметки

1. Для работы на macOS нужно установить `rumps`:
```console
pip install rumps
```

2. Также на последней версии macOS 10.14.5 (18F132) возникает `NSException`.