class Car:
    def __init__(self, name: str, price, speed):
        self.name = name
        self.price = float(price)
        self.speed = int(speed)

    def get_info(self):
        return f'{self.name}, price: {self.price}, max speed {self.speed}'


if __name__ == '__main__':
    cars = []
    for _ in range(2):
        name_user = input('Name: ')
        price_user = input('Price: ')
        speed_user = input('Max speed: ')
        cars.append(Car(name_user, price_user, speed_user))
        print('--' * 10)

    for car in sorted(cars, key=lambda c: c.price, reverse=True):
        print(car.get_info())

    for car in sorted(cars, key=lambda c: c.speed):
        print(car.get_info())


def test_class_car():
    car_test = Car(name='Ford', price=1000, speed=160)

    assert isinstance(car_test, Car)
    assert car_test.name == 'Ford'
    assert car_test.price == 1000
    assert car_test.speed == 160
