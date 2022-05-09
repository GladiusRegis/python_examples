names = [
    'Emily',
    'Mary',
    'Lily',
    'Alice',
    'Rose',
    'Sarah',
    'Cindy',
    'Janet',
    'Lucy',
    'Tracy',
]


for id, name in enumerate(names):
    print(f'{id}. {name}')

try:
    number = int(input('Which name you choose: '))
    print(names[number])
except IndexError as error:
    print('There is no such name on the list!')
    print(error)

except (TypeError, ValueError) as error:
    print('Enter a number!')
    print(error)

