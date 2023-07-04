number_list = [1, 2, 3, 4, 5]
print(number_list)
misc_list = ['Aditya', 101]
big_list = ['Adi', 'Patro', 1, 2, 3]
print(misc_list)
combined_list = number_list + misc_list
print(combined_list)
misc_list[0] = misc_list[0].upper()
print(misc_list)
print(big_list[2:])
print(big_list)

# Nested List
mixed_list = [1, 2, [3, 4]]
print(mixed_list)
print("Inner List = ", mixed_list[2])
print("Inner List 1st element = ", mixed_list[2][0])
print("Inner List last element = ", mixed_list[2][-1])


# List Methods
number_list.append(6)
print(number_list)
number_list.append('API')
print(number_list)
number_list.pop()
print(number_list)
number_list.pop(2)
print(number_list)
print("Size of the number list = ", len(number_list))
duplicate_list = [1, 2, 2, 2, 2, 1]
print("Number of Occurrence = ", duplicate_list.count(2))
unsorted_list = [8, 5, 1, 4, 0]
unsorted_list.sort()
print(unsorted_list)
unsorted_list.reverse()
print(unsorted_list)
unsorted_list.remove(0)
print(unsorted_list)
