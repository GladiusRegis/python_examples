class Person:
    def __init__(self, first_name: str, last_name: str):
        self.last_name = last_name
        self.first_name = first_name

    # def __str__(self):
    #     return f'{self.first_name} {self.last_name}'


me = Person('Gladius', 'Regis')
print(me)
print(me.first_name)

test = str(me)
print(type(test))

