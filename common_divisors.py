def find_divisors(number):
    # divisors = set()
    # for divisor in range(2, number + 1)
    #     if number % divisor == 0:
    #         divisors.add(divisor)
    # return divisors
    return {divisor for divisor in range(2, number + 1) if number % divisor == 0}

# def calculate_common_divisor(number_1, number_2, offset=2):
#     common_divisors = find_divisors(number_1) & find_divisors(number_2)
#     common_divisors = [divisor for divisor in common_divisors if divisor >= offset]
#     return sorted(list(common_divisors))


def calculate_common_divisor(set_1, set_2, offset=2):
    return sorted([div for div in (find_divisors(set_1) & find_divisors(set_2)) if div > offset])


test1 = calculate_common_divisor(3, 6)
print(test1)

test2 = calculate_common_divisor(3, 6, 4)
print(test2)

test3 = calculate_common_divisor(16, 8)
print(test3)



