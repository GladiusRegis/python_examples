def calculate_common_divisor(number_1, number_2, offset):

    set_1 = {number for number in range(2, number_1) if number_1 % number == 0}
    set_2 = {number for number in range(2, number_2) if number_2 % number == 0}

    bigger_than = [bigger for bigger in (set_1 & set_2) if bigger > offset]

    return bigger_than


test1 = calculate_common_divisor(3, 6)
print(test1)

test2 = calculate_common_divisor(3, 6, 4)
print(test2)

test3 = calculate_common_divisor(16, 8)
print(test3)



