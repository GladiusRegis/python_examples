list_1 = [1, 2, 3, 4, 4, 5, 6, 6]


def give_even(list_number: list) -> list:
    return [even for even in list_number if even % 2 == 0]


print(give_even(list_1))
