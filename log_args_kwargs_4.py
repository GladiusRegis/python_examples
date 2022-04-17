def log(*args, **kwargs):
    for arg in args:
        print(type(arg), arg)
    print(args)
    print(kwargs)


log('1', 2, 3, hello='hallelujah')
