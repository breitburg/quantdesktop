# Реализация для macOS
# TODO: Перейти на универсальную реализацию

from rumps import App, clicked
from config import config


class StatusBarApp(App):
    def __init__(self):
        super().__init__('Quantify', icon='assets/icon_mac.png', quit_button='Выход')
        self.menu = ['Мышь', 'Клавиатура']

        for item in self.menu.items():
            # Ставим значение всех чекбоксов на True
            item[1].state = 1

    @clicked('Мышь')
    def mouse(self, sender):
        sender.state = not sender.state
        config.set_value('mouse', sender.state)

    @clicked('Клавиатура')
    def keyboard(self, sender):
        sender.state = not sender.state
        config.set_value('keyboard', sender.state)


# Создаем инстанс приложения
app = StatusBarApp()
