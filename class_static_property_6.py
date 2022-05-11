class Student:
    NEXT_ID = 1

    def __init__(self, first_name, last_name):
        self.id = Student.NEXT_ID
        self.last_name = last_name
        self.first_name = first_name
        Student.NEXT_ID += 1

    def hello(self):
        return f'{self.id}. {self.first_name} {self.last_name}'




