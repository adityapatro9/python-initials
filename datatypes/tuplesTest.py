# Tuples are same as list, but it immutable.
t = (1, 2, 3, 4, 1, 'Aditya')
print(t)
print(t[0])
print(t[-1])
print(t.count(1))
print(t.index('Aditya'))
print(t.index(1))

# t[0] = 0 , We cant as its immutable
