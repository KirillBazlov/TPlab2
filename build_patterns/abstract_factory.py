from abc import ABC, abstractmethod

# общий абстрактный класс кнопки
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass
# Конкретный продукт кнопки win
class WinButton(Button):
    def paint(self):
        return "Windows Button"

# Конкретный продукт кнопки mac
class MacButton(Button):
    def paint(self):
        return "Mac Button"
# общая абстрактная фабрика
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass
# Конкретный фабрика win
class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()
# Конкретный фабрика mac
class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

# Использование
def render_ui(factory: GUIFactory):
    button = factory.create_button()
    print(button.paint())

render_ui(WinFactory())  # Windows Button
render_ui(MacFactory())  # Mac Button
