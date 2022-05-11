from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_name(self):
        pass

a = Item('ABC')
# TypeError: Can't instantiate abstract class Item with abstract method get_name