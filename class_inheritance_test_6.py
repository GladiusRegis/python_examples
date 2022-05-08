class User:
    def login(self):
        return 'Login'


class Teacher(User):
    def run(self):
        return 'I teach!'


class Student(User):
    def run(self):
        return 'I study!'

    def testing(self):
        return self.login()


aaron = Teacher()
print(aaron.run())
print(aaron.login())

johny = Student()
print(johny.run())
print(johny.login())


class Parent:
    def get_type(self):
        return 'parent'


class Child(Parent):
    def get_type(self):
        return 'child'


sample = Child()
print(sample.get_type())
