class Chair:
    def sit_on(self):
        pass

class Sofa:
    def lie_on(self):
        pass

class ModernChair(Chair):
    def sit_on(self):
        return "Сидим на стуле"

class ModernSofa(Sofa):
    def lie_on(self):
        return "Лежим на диване"

class ClassicChair(Chair):
    def sit_on(self):
        return "Сидим на классическом стуле"

class ClassicSofa(Sofa):
    def lie_on(self):
        return "Лежим на классическом диване"

class FurnitureFactory:
    def create_chair(self):
        pass

    def create_sofa(self):
        pass

class ModernFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()

class ClassicFactory(FurnitureFactory):
    def create_chair(self):
        return ClassicChair()

    def create_sofa(self):
        return ClassicSofa()
