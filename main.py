from kivy.app import App
from kivy.lang import Builder
from kivy.properties import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import CoverBehavior

from models import Pizza


class PizzaWidget(BoxLayout):
    name = StringProperty()
    ingredients = StringProperty()
    price = NumericProperty()
    vegetarian = BooleanProperty()


class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pizzas = [
            Pizza('4 Formaggi', 'Tomato sauce, mozzarella, taleggio, gorgonzola, parmesan', 11.00, True),
            Pizza('Vegetarian', 'Tomato sauce, mozzarella, peppers, onions, mushrooms', 8.50, True),
            Pizza('Casa', 'Tomato sauce, mozzarella, broccoli, homemade sausage', 11.50, False),
            Pizza('Salmone', 'Tomato sauce, mozzarella, taleggio, gorgonzola, parmesan', 13.99, False)
        ]

    def on_parent(self, widget, parent):
        l = [pizza.get_dictionary() for pizza in self.pizzas]
        self.recycleView.data = l


with open("pizzascr.kv", encoding='utf8') as f:
    Builder.load_string(f.read())


class PizzaApp(App):
    def build(self):
        return MainWidget()


PizzaApp().run()
