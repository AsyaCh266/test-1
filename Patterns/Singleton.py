class SingletonMeta(type):
    _instances = {}

    def _call(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super()._call(*args, **kwargs)
        return cls._instances[cls]


class AppSettings(metaclass=SingletonMeta):
    def _init(self):
        self.theme = "dark"
        self.language = "ru"
