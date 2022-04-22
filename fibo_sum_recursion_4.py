def fibonacci_sum(n):
    if n == 0:
        return 0

    if n == 1:
        return 0

    return fibonacci_sum(n - 1) + fibonacci_sum(n - 2) + 1


def test_fibonacci_sum():
    assert fibonacci_sum(0) == 0
    assert fibonacci_sum(1) == 0
    assert fibonacci_sum(2) == 1
    assert fibonacci_sum(3) == 2
    assert fibonacci_sum(5) == 0 + 1 + 1 + 2 + 3
    assert fibonacci_sum(8) == 0 + 1 + 1 + 2 + 3 + 5 + 8 + 13