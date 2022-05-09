class Person:
    def __init__(self, first_name, last_name):
        self._last_name = last_name
        self._first_name = first_name

    def first_name(self):
        return self._first_name

    def last_name(self):
        return self._last_name

    def details(self):
        return f'{self._first_name} {self._last_name}'


person = Person('Barney', 'Rubble')
print(person.first_name())
print(person.last_name())
print(person.details())


class Person1:
    def __init__(self, first_name, last_name):
        self._last_name = last_name
        self._first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def details(self):
        return f'{self._first_name} {self._last_name}'


person = Person1('test', 'test')
print(person.first_name)
print(person.last_name)
print(person.details)
