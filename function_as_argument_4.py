from collections.abc import Callable

# Callable[[argument_type], return_type]


def do_something(data: list, f: Callable[[list], int]):
    return f(data)


print(do_something([1, 2, 3], sum))
print(do_something([1, 2, 3], len))

