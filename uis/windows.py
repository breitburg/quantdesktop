from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image
from config import config

state = False

class State:
    mouse = True
    keyboard = True

    def __init__(self):
        return


state = State()


def on_clicked_mouse(icon, item):
    global state
    state.mouse = not item.checked
    config["mouse"] = state.mouse


def on_clicked_keyboard(icon, item):
    global state
    state.keyboard = not item.checked
    config["keyboard"] = state.keyboard

image = Image.open("assets/icon_win.png")

def run():
    icon('Quantify', image, menu=menu(
        item(
            'Мышь',
            on_clicked_mouse,
            checked = lambda item: state.mouse
        ),
        item(
            'Клавиатура',
            on_clicked_keyboard,
            checked=lambda item: state.keyboard
        )
        )).run()