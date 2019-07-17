class BaseModule:
    def __init__(self, name):
        self.name = name

    def update(self):
        pass


from .mouse import MouseModule
to_load = [MouseModule()]