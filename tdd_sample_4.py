def rectangle_area(a: int, b: int) -> int:
    return a * b


def test_rectangle_area():
    assert rectangle_area(2, 10) == 20
    assert rectangle_area(5, 3) == 15

