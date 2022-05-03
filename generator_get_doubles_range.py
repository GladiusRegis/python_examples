def get_doubles(numbers: range):
    results = []
    for i in numbers:
        results.append(i+i)
    return results


for n in get_doubles(range(1, 11)):
    print(f'Wynik wynosi {n}')


def get_double2(numbers: range):
    for i in numbers:
        print(f'Iteruje.. liczbę dla  {i}')
        yield i + i


results = get_double2((range(10, 40)))
print(next(results))
print(next(results))
print(next(results))
print(next(results))


def get_double3(numbers: range):
    for i in numbers:
        print(f'Iteruje.. liczbę dla  {i}')
        yield i + i


for n in get_double3(range(1, 11)):
    print(f'Wynik wynosi {n}')
