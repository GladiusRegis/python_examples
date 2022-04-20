numbers = [1, 5, 10, 9, 7]

doubles_lc = [n + n for n in numbers]

doubles_l = map(lambda n: n + n, numbers)

print(doubles_lc)
print(list(doubles_l))

filtered_lc = [n for n in numbers if n % 2 == 0]

filtered_l = filter(lambda n: n % 2 == 0, numbers)

print(filtered_lc)
print(list(filtered_l))


numbers2 = [(1, 2), (3, 4), (5, 6)]

total_lc = sum([a * b for a, b in numbers2])
print(total_lc)

from functools import reduce  # reduce należy zaimportować
total_l = reduce(lambda sum, a: sum + a[0] * a[1], numbers2, 0)
# pierwszy argument funkcja - lambda, drugi argument lista, trzeci argument wartość początkowa 0
# na początku funkcja sum będzie zawierała wartość początkową 0
# bez trzeciego argumentu dostaniemy None
print(total_l)
