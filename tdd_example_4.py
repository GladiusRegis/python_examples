def add_numbers(a: int, b: int) -> int:
    return a + b


def test_add_numbers():
    # Given
    a = 2
    b = 3

    # When
    value = add_numbers(a, b)

    # Then
    assert value == 5

