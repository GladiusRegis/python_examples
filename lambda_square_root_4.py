# from math import sqrt
a = [16, 36, 25, 49]


def map_and_filter(numbers: list) -> list:
    # sqrts = map(sqrt, numbers)
    sqrts = map(lambda x: x ** 0.5, numbers)
    return list(filter(lambda x: x % 2 == 0, sqrts))


def test_map_and_filter():
    b = [16, 36, 25, 49]
    assert map_and_filter(b) == [4, 6]


if __name__ == '__main__':
    print(map_and_filter(a))
