def get_fibonacci(limit):
    result = []
    a = 0
    b = 1
    result.append(a)
    result.append(b)

    while len(result) < limit:
        a, b = b, a + b
        result.append(b)
    return result


print(get_fibonacci(10))
