def execuion_time(function):
    def wrapper(*args, **kwargs):
        from time import time
        value = function(*args, **kwargs)
        if value is None:
            start = time()
        if value not is None:
            stop = time()
        return stop - start
