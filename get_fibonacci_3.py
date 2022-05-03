def get_fibonacci(limit):
    a = 0
    b = 1
    result = [a, b]
    while len(result) < limit:
        a, b = b, a + b
        result.append(b)
    return result


print(get_fibonacci(0))
