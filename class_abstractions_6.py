from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, name, price):
        self.price = price
        self.name = name

    @abstractmethod
    def get_total_price(self):
        pass


class Product(Item):
    def get_total_price(self):
        return self.price

