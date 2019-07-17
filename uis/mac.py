from rumps import App, clicked
from config import config


class StatusBarApp(App):
    def __init__(self):
        super().__init__('Quantify', icon='assets/icon_mac.png', quit_button='Выход')
        self.menu = ['Мышь', 'Клавиатура']

        for item in self.menu.items():
            item[1].state = 1

    @clicked('Мышь')
    def mouse(self, sender):
        sender.state = not sender.state
        config['mouse'] = sender.state

    @clicked('Клавиатура')
    def keyboard(self, sender):
        sender.state = not sender.state
        config['keyboard'] = sender.state

app = StatusBarApp()
