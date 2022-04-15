def find_divisors(a: int) -> set:
    return {d for d in range(1, a + 1) if a % d == 0}


def find_greatest_divisor(a: int, b: int) -> int:
    div_a = find_divisors(a)
    div_b = find_divisors(b)
    return max(div_a & div_b)


print(find_greatest_divisor(32, 48))
