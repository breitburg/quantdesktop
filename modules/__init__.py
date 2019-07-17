class BaseModule:
    def __init__(self):
        pass

    def update(self):
        pass


from .mouse import MouseModule
to_load = [MouseModule()]