__version__ = '1.0.15'
url_endpoint = 'http://195.201.111.238:8001/'  # URL для отправки данных


class Config:
    # Параметры которые мы будем изменять
    properties = {
        'keyboard': True,
        'mouse': True,
        'processes': True
    }

    # Метод для утановки значения
    def set_value(self, title: str, value: bool):
        self.properties[title] = value

    # Метод получения значения
    def get_value(self, title: str):
        assert title in self.properties
        return self.properties[title]


# Создаем инстанс конфига
config = Config()
