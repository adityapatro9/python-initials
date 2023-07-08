def add_numbers(a: int, b: int, c: int):
    if a is not None and b is not None and c is not None:
        return a + b + c
    elif a is None and b is not None and c is not None:
        return b + c
    elif a is not None and b is None and c is not None:
        return a + c
    elif a is not None and b is not None and c is None:
        return a + b
    else:
        return 'Unknown Error'


def even_odd(num: int):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


def even_odd_list(num_list: list):
    print(num_list)
    index = 0
    for num in num_list:
        if type(num) == int:
            if num % 2 == 0:
                num_list[index] = 'EVEN'
            else:
                num_list[index] = 'ODD'
        else:
            num_list[index] = '*'
        index += 1
    print(num_list)


print(add_numbers(2, 2, None))
print(even_odd(5))
even_odd_list(list(range(0, 11)))
even_odd_list([1,2,3,'Aditya',6,9])
