attendance = ['X', 'O', 'X', 'X', 'O', 'O']
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_ranged_list = list(range(1, 11))

if attendance.count('X') >= 3:
    print('PASS')
else:
    print('FAIL')

for att in attendance:
    if att == 'X':
        print(f'{att} - PASS')
    else:
        print(f'{att} - FAIL')

print('*************************************')

for num in num_ranged_list:
    if num % 2 == 0:
        print(f'{num} - EVEN')
    else:
        print(f'{num} - ODD')

print('*************************************')

tup_list = [(1, 'Ronaldo'), (2, 'Messi'), (3, 'Pele'), (4, 'Neymar'), (5, 'Suarez')]
for a, b in tup_list:
    print(f'{a} - {b}')

print('*************************************')

for ch in 'Aditya':
    print(ch)

print('*************************************')

x = 0
while x < 5:
    print(f'The Value = {x}')
    x += 1
else:
    print('Ends Here')

print('*************************************')

cmd_list = ['if', 'elif', 'continue', 'else', 'while', 'for', 'break', 'end']

for cmd in cmd_list:
    if cmd == 'continue':
        continue
    elif cmd == 'break':
        break
    else:
        print(cmd)

print('*************************************')

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
zipped_list = list(zip(list1, list2))
print(f'Zipped list = {zipped_list}')

print('*************************************')

from random import shuffle, randint

num_ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(num_ordered_list)
print(f'Shuffled list : {num_ordered_list}')

index = 0
search = randint(1, 11)
print(f'KILL -> {search}')
while index < len(num_ordered_list):
    if num_ordered_list[index] == search:
        print(f'{num_ordered_list[index]} - HIT')
        break
    else:
        print(f'{num_ordered_list[index]} - MISS')
    index += 1

print('*************************************')

# enumerate provides tuple with index, no need to maintain index variable
for item in enumerate('Aditya'):
    print(item)

print('*************************************')

print('b' in 'Aditya')
print(1 in num_list)

print('*************************************')

print(f'Max = {max(num_list)}')
print(f'Min = {min(num_list)}')

print('*************************************')

# Type Casting
num1 = '2'
num2 = '3'
print(type(num1))
summation = int(num1) + int(num2)
print(f'Sum = {summation}')
print(type(summation))

print('*************************************')

# List Comprehension

comp_list = [letter for letter in 'Aditya']
print(comp_list)

even_list = [num for num in range(0, 11) if num % 2 == 0]
print(even_list)

lists = [num if num % 2 == 0 else 'ODD' for num in range(0, 11)]
print(lists)

print('*************************************')

# Nested For Loop

n = 6
for i in range(0,n):
    for j in range(0,i):
        print('*',end="")
    print('\n')
