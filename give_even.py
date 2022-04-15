list_1 = [1, 2, 3, 4, 4, 5, 6, 6]


def filter_even(numbers: list) -> list:
    return [even for even in numbers if even % 2 == 0]


print(filter_even(list_1))
