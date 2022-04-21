def to_string(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        if isinstance(value, list):
            return [str(element) for element in value]
        else:
            return str(value)

    return wrapper


@to_string
def return_int():
    return 1


@to_string
def return_list():
    return [1, 2, 3]

