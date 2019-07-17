class Config:
    properties = {
        'keyboard': True,
        'mouse': True
    }

    def set_value(self, title: str, value: bool) -> None:
        self.properties[title] = value

    def get(self, title: str) -> bool:
        assert title in self.properties
        return self.properties[title]

config = Config()