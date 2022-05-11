from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: float
    discount: float


class Collection:
    def __init__(self):
        self.items = []

    @classmethod
    def create_with_items(cls, *args):
        collection = cls()
        collection.items.extend(args)

        return collection


i1 = Item('Chanel jacket', 2500, 0.1)
i2 = Item('dolce gabbana jacket', 3200, 0.2)

col = Collection.create_with_items(i1, i2)
print(col.items)







