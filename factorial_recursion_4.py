def calculater_factorial(number):
    if number == 0:
        return 1

    return number * calculater_factorial(number - 1)


def test_power_zero():
    assert calculater_factorial(0) == 1


def test_power():
    assert calculater_factorial(1) == 1
    assert calculater_factorial(5) == 5 * 4 * 3 * 2 * 1





