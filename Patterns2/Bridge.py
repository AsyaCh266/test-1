from abc import ABC, abstractmethod

class Control(ABC):
    @abstractmethod
    def operate(self):
        pass

class RemoteControl(Control):
    def operate(self):
        return "Управление с пульта"

class VoiceControl(Control):
    def operate(self):
        return "Голосовое управление"

class Device(ABC):
    def _init(self, control: Control):
        self.control = control

    @abstractmethod
    def use(self):
        pass

class TV(Device):
    def use(self):
        return f"Телевизор: {self.control.operate()}"

tv = TV(RemoteControl())
print(tv.use())

tv = TV(VoiceControl())
print(tv.use())
