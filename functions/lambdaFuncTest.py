from builtins import map

num_list = [1, 2, 3, 4, 5]
string_list = ['Aditya', 'Patro', 'Messi', 'Ronaldo']


def square(num):
    return num ** 2


def splicer(stringname):
    if len(stringname) % 2 == 0:
        return 'EVEN'
    else:
        return stringname[0]


print(list(map(square, num_list)))
print(list(map(splicer, string_list)))

print('#####################################')


def check_even(num):
    return num % 2 == 0


print(list(filter(check_even, num_list)))

print('#####################################')

sqr = lambda num: num ** 2
print(sqr(20))

print(list(map(lambda name: name[0], string_list)))
print(list(map(lambda name: name[::-1], string_list)))
