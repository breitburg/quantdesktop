class Config:
    # Параметры которые мы будем изменять
    properties = {
        'keyboard': True,
        'mouse': True
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
