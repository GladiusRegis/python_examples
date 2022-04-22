from math import pi


def to_fixed(number):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            return round(func(*args, **kwargs), number)

        return inner_wrapper

    return wrapper


@to_fixed(3)
def show_me_pi_three():
    return pi


@to_fixed(2)
def show_me_pi_two():
    return pi
