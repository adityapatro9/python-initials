try:
    res = 10 / 0
except Exception as exp:
    print('Exception Caught!', exp)

print('*********************************')

num_list = [1, 2, 3, 4, 5]
try:
    res = num_list[10]
    print(res)
except Exception as exp:
    print('Exception Caught!', exp)
else:
    print('Else Block Executed!')
finally:
    print('Finally Executed')


