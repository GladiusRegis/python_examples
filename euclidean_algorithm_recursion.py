def euclidean_algorithm(a: int, b: int) -> int:
    while b != 0:
        c = a % b
        a, b = b, c

    return a


def test_euclidean_algorithm():
    assert euclidean_algorithm(4, 8) == 4
    assert euclidean_algorithm(8, 4) == 4
    assert euclidean_algorithm(27, 36) == 9
    assert euclidean_algorithm(36, 27) == 9


print(euclidean_algorithm(27, 36))
