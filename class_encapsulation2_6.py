class Student:
    def __init__(self, data: str, semestr: int):
        self._data = data
        self._semestr = semestr

    def __str__(self):
        return f'{self._data}, term: {self._semestr}'


student = Student('Smith', 1)
print(student)

print(student._data)  # encapsulation
print(student._semestr)  # encapsulation

