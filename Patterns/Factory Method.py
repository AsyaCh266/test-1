class Transport:
    def deliver(self):
        pass


class Truck(Transport):
    def deliver(self):
        return "Доставка грузовиком"


class Ship(Transport):
    def deliver(self):
        return "Доставка кораблём"


class TransportFactory:
    @staticmethod
    def create_transport(type_):
        if type_ == "truck":
            return Truck()
        elif type_ == "ship":
            return Ship()
        else:
            raise ValueError("Неизвестный транспорт")
