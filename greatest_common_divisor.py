def find_divisors(a: int) -> set:
    return {d for d in range(1, a + 1) if a % d == 0}


def find_greatest_divisor(a: int, b: int) -> int:
    div_a = find_divisors(a)
    div_b = find_divisors(b)
    return max(div_a & div_b)


"""Algorytm Euklidesa"""


def algorithm_euclidean(number1: int, number2: int) -> int:
    # faster method for large numbers
    # if number1 < number2:
    #     x = number1
    #     number1 = number2
    #     number2 = x

    done = False
    while not done:
        rest = number1 % number2
        if rest == 0:
            done = True
            continue
        number1, number2 = number2, rest
    return number2


print(find_greatest_divisor(96, 16))
print(algorithm_euclidean(8, 4))

