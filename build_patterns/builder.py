# Продукт
class Pizza:
    def __init__(self):
        self.dough = ""
        self.sauce = ""
        self.topping = ""

    def __str__(self):
        return f"Pizza{{dough='{self.dough}', sauce='{self.sauce}', topping='{self.topping}'}}"


# Интерфейс строителя
from abc import ABC, abstractmethod

class PizzaBuilder(ABC):
    def __init__(self):
        self.pizza = Pizza()

    @abstractmethod
    def build_dough(self):
        pass

    @abstractmethod
    def build_sauce(self):
        pass

    @abstractmethod
    def build_topping(self):
        pass

    def get_result(self):
        return self.pizza


# Конкретный строитель: Гавайская пицца
class HawaiianPizzaBuilder(PizzaBuilder):
    def build_dough(self):
        self.pizza.dough = "cross"

    def build_sauce(self):
        self.pizza.sauce = "mild"

    def build_topping(self):
        self.pizza.topping = "ham+pineapple"


# Конкретный строитель: Пицца пепперони
class SpicyPizzaBuilder(PizzaBuilder):
    def build_dough(self):
        self.pizza.dough = "thin"

    def build_sauce(self):
        self.pizza.sauce = "hot"

    def build_topping(self):
        self.pizza.topping = "pepperoni"


# Директор
class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def construct_pizza(self):
        self.builder.build_dough()
        self.builder.build_sauce()
        self.builder.build_topping()


# Пример использования
if __name__ == "__main__":
    # Создаём гавайскую пиццу
    hawaiian_builder = HawaiianPizzaBuilder()
    director = PizzaDirector(hawaiian_builder)
    director.construct_pizza()
    hawaiian_pizza = hawaiian_builder.get_result()
    print(hawaiian_pizza)

    # Создаём острую пиццу
    spicy_builder = SpicyPizzaBuilder()
    director = PizzaDirector(spicy_builder)
    director.construct_pizza()
    spicy_pizza = spicy_builder.get_result()
    print(spicy_pizza)
