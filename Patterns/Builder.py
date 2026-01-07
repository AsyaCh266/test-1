class Pizza:
    def _init(self):
        self.dough = None
        self.sauce = None
        self.topping = None

    def _str(self):
        return f"{self.dough}, {self.sauce}, {self.topping}"


class PizzaBuilder:
    def _init(self):
        self.pizza = Pizza()

    def add_dough(self, dough):
        self.pizza.dough = dough
        return self

    def add_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self

    def add_topping(self, topping):
        self.pizza.topping = topping
        return self

    def build(self):
        return self.pizza
