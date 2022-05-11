class Person:
    def __init__(self, first_name: str, last_name: str):
        self.last_name = last_name
        self.first_name = first_name

    @classmethod
    def from_row(cls, row: str):
        # John Doe
        first_name, last_name = row.strip().split(';')
        return cls(first_name, last_name)


p = Person('John', 'Doe')
print(p.first_name)
print(p.last_name)
p = Person.from_row('John;Doe')
print(p.first_name)
print(p.last_name)
