class RealFile:
    def read(self):
        return "Содержимое файла"


class FileProxy:
    def _init(self, has_access):
        self.has_access = has_access
        self.real_file = RealFile()

    def read(self):
        if self.has_access:
            return self.real_file.read()
        return "Доступ запрещён"


proxy = FileProxy(has_access=False)
print(proxy.read())

proxy.has_access = True
print(proxy.read())
