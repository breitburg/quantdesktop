url_endpoint = 'http://192.168.0.3:8001/'  # URL для отправки данных


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
