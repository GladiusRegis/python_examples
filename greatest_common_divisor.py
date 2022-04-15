def give_greatest_divisor(number1: int, number2: int) -> int:
    set_1 = {number for number in range(2, number1 + 1) if number1 % number == 0}
    set_2 = {number for number in range(2, number2 + 1) if number2 % number == 0}
    list_common = list(set_1 & set_2)

    divisor = 0 if list_common == [] else max(list_common)
    return divisor


print(give_greatest_divisor(15, 21))
