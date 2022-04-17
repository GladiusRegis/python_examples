""" *args """


def average(*args):
    print(args)
    return sum(args) / len(args)


print(average(10, 20, 30))


def print_args(a, b, *others):
    print('a', a)
    print('b', b)
    print(others)


"""**kwargs"""


def save(filename, **kwargs):
    print(filename)
    print(kwargs)


save('students.txt', first_name='John', last_name='Smith')

