from math import pi


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2

    def calculate_circumference(self):
        return 2 * pi * self.radius


if __name__ == '__main__':
    radius_user = float(input('Enter a radius: '))
    circle_user = Circle(radius_user)
    print(f'Area = {circle_user.calculate_area():.2f}')
    print(f'Circumference{circle_user.calculate_circumference():.2f}')


def test_circle_area():
    # given
    r = 5
    c = Circle(r)

    # when
    field = c.calculate_area()

    # then
    assert field == pi * r * r


def test_circle_circumference():
    # given
    r = 5
    c = Circle(r)

    # when
    circum = c.calculate_circumference()

    # then
    assert circum == 2 * pi * r
