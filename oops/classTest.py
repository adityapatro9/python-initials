class Student:
    college = 'ITER'

    def __init__(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact

    def getdetails(self):
        return self.name + '-' + str(self.age) + '-' + self.contact + '-' + self.college

    def addnumbers(self, num_list):
        return sum(num_list)


s1 = Student('Aditya', 29, '9040300382')
s2 = Student('Messi', 35, '8261042910')

print(type(s1))
print(type(s1) == type(s2))
print(s2.getdetails())
print(s1.getdetails())

print(s1.addnumbers([1, 2, 3, 4, 5]))

print(Student.college)
