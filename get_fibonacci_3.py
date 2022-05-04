def get_fibonacci(limit):
    # if limit == 0:
    #     return[]
    # if limit == 1:
    #     return[0]
    a = 0
    b = 1
    result = [a, b]
    while len(result) < limit:
        a, b = b, a + b
        result.append(b)
    return result[:limit]


print(get_fibonacci(0))
