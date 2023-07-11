class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def who_am_i(self):
        print('I am Human')

    def job(self):
        raise NotImplementedError("Implement this in subclass")


class Engineer(Human):

    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def details(self):
        return self.name + '-' + str(self.age) + '-' + self.department

    def who_am_i(self):
        print('I am Engineer')

    def job(self):
        return 'IT'

    def __str__(self):
        return f'{self.name}-{self.age}-{self.department}'

    def __len__(self):
        return self.age

    def __del__(self):
        print('Engineer Deleted')


e = Engineer('Aditya', 29, 'Banking')
print(e.details())
print(e.who_am_i())
print(type(e))
print(e.job())
print(e)
print(len(e))
del e
print(e)
