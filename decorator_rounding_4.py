def rounding_float(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        return round(value, 2)

    return wrapper


@rounding_float
def division(a: int, b: int) -> float:
    return a / b


print(division(5, 3))
