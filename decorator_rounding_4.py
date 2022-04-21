def round_it(func):
    def wrapper(*args, **kwargs):
        return round(func(*args, **kwargs), 2)

    return wrapper


def test_round_it():
    @round_it
    def function(value):
        return value

    assert function(3.448) == 3.45
    assert function(3.5000) == 3.5


@round_it
def division(a: int, b: int) -> float:
    return a / b


print(division(5, 3))
