class Car:
    def __init__(self, name: str, price, speed):
        self.name = name
        self.price = float(price)
        self.speed = int(speed)

    def get_info(self):
        return f'{self.name}, price: {self.price}, max speed {self.speed}'


class Collection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_items(self, key, reverse=False):
        return sorted(self.items, key=key, reverse=reverse)


if __name__ == '__main__':
    collection = Collection()

    for _ in range(5):
        name_user = input('Name: ')
        price_user = input('Price: ')
        speed_user = input('Max speed: ')
        collection.add_item(Car(name_user, price_user, speed_user))
        print('--' * 10)
    print('Sorted by price:')
    for car in collection.get_items(key=lambda c: c.price, reverse=True):
        print(car.get_info())
    print('Sorted by speed')
    for car in collection.get_items(key=lambda c: c.speed):
        print(car.get_info())


def test_class_car():
    car_test = Car(name='Ford', price=1000, speed=160)

    assert isinstance(car_test, Car)
    assert car_test.name == 'Ford'
    assert car_test.price == 1000
    assert car_test.speed == 160
