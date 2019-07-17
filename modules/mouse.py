from . import BaseModule

from pynput.mouse import Controller
mouse = Controller()


class MouseModule(BaseModule):
    def __init__(self):
        pass

    def update(self):
        return mouse.position
