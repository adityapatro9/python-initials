a: int = 2
b: int = 3
c: int = 8
d: int = 2

summed: int = a + b
power: int = a ** b

print("sum=", summed)

name: str = "Aditya"

rain: bool = True

summed = c + d

print("sum=", summed)
print("name=", name)
print(name[1])
print(name[-1])
print("rain=", rain)
print("powered=", power)
print(type(a))

e = 10
print("DataType of e = ", type(e))
e = "Aditya"
print("DataType of e = ", type(e))
print("length of name=", len(name))

print("************ Slicing Test Start ************")
print(name[1:])
print(name[1:4])
print(name[:])
print(name[:4])
print(name[0::2])
print("Hello World"[8:9])
print("Hello World"[8])
print("************ Slicing Test End ************")
print('\n')
print("************ String Properties Test Start ************")
print(name * 10)  # Repeats the name variable 10 times
print(name.isupper())
print(name.islower())
print("Aditya Patro".split())
print(name.upper())
print(name.lower())
print(name)
print("This is the Reality".split('i'))
print("************ String Properties Test end ************")
print('\n')
print("************ String Formatting Test Start ************")
# Old Format calls
print("My name is {} {}".format("Aditya", "Patro"))
print("My name is {1} {0}".format("Aditya", "Patro"))
print("My name is {0} {0}".format("Aditya", "Patro"))
print("My name is {a} {p}".format(a="Aditya", p="Patro"))
res = 10 / 3
print("The Result was = {r:1.3f}".format(r=res))  # {value:width.precision f}

# New format call
print(f"My name is = {name}")
print(f"My name is {name}.And today 10/3 = {res:1.3f}")
print("************ String Formatting Test end ************")
