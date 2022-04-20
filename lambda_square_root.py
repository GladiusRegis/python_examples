number_list = [16, 36, 25, 49]


def given_square_root(numbers: list) -> list:
    square_root = list(map(lambda n: n * n, numbers))
    return square_root


def choose_even(number: list) -> list:
    return list(map(lambda e: e % 2 == 0, given_square_root(number_list)))

    def test_given_square_root():
        assert given_square_root([2, 4]) == [4, 8]
        assert given_square_root([3]) == 9

    def test_choose_even():
        assert choose_even([2, 3, 5]) == [2]

    if __name__ == '__main__':
        print(choose_even(number_list))
