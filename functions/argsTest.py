# *args returns a Tuple
# **kwargs return a Dictionary


def multi_args(*args):
    print(args)
    return sum(args)


def key_multi_args(**kwargs):
    print(kwargs)
    return kwargs.keys()


def mixed_args(*args, **kwargs):
    print(args)
    print(kwargs)


print(multi_args(1, 2, 3, 4, 4))
print(key_multi_args(name='Aditya', age=29), '\n')
print(mixed_args(1, 2, name='Aditya', age=29))


def myfunc(name):
    index = 0
    res: str = ''
    for i in name:
        if index % 2 == 0:
            res += i.upper()
        else:
            res += i.lower()
        index += 1
    return res


print('\n')
print(myfunc('Aditya'))
