def calculate_common_division(number_1, number_2, start=1):

    set_1 = {number for number in range(2, number_1) if number_1 % number == 0}
    set_2 = {number for number in range(2, number_2) if number_2 % number == 0}

    bigger_than = [bigger for bigger in (set_1 & set_2) if bigger > start]

    return set_1, set_2, set_1 & set_2, bigger_than


print(calculate_common_divisior(100, 200))



