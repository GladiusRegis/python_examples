def count_numbers(numbers: list, count_odd: bool = True, count_even: bool = True):
    odds = [number for number in numbers if number % 2 != 0]
    even = [number for number in numbers if number % 2 == 0]

    total = len(odds) if count_odd else 0
    total += len(even) if count_even else 0

    # Kacper way
    total2 = 0 if not count_odd else len(odds)
    total2 += 0 if not count_even else len(even)

    return total, total2


print(count_numbers([2, 4, 6, 8, 5], count_odd=False, count_even=True))


