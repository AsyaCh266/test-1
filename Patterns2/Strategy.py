from abc import ABC, abstractmethod

class Handler(ABC):
    def _init(self, successor=None):
        self.successor = successor

    @abstractmethod
    def handle(self, request):
        pass


class SupportHandler(Handler):
    def handle(self, request):
        if request == "support":
            return "Запрос обработан службой поддержки"
        elif self.successor:
            return self.successor.handle(request)


class ManagerHandler(Handler):
    def handle(self, request):
        if request == "manager":
            return "Запрос обработан менеджером"
        elif self.successor:
            return self.successor.handle(request)


class DirectorHandler(Handler):
    def handle(self, request):
        return "Запрос обработан директором"

chain = SupportHandler(ManagerHandler(DirectorHandler()))
print(chain.handle("manager"))
