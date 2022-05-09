class Person:
    def __init__(self, first_name, last_name):
        self.details = f'{first_name} {last_name}'


class Student(Person):
    def __init__(self, first_name, last_name, semester):
        super().__init__(first_name, last_name)
        self.semester = semester


john = Student('John', 'Blacksmith', 2)
print(john.details)
print(john.semester)


