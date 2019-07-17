from . import BaseModule

from pynput.mouse import Controller
mouse = Controller()


class MouseModule(BaseModule):
    def __init__(self):
        super().__init__(name='mouse')

    def update(self):
        return mouse.position
