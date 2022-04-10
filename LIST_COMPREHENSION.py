"""LIST COMPREHENSION"""

"""podwajanie wartości"""

doubles = []
for n in range(1, 11):
    doubles.append(n + n)
print(doubles)

print([n + n for n in range(1, 11)])

"""building a list"""

new_list = []
for n in range(1, 11):
    if n % 2 == 0:
        new_list.append('even')
    else:
        new_list.append('odd')

print(new_list)

new_list = ['even' if n % 2 == 0 else 'odd' for n in range(1, 11)]
print(new_list)

"""filtering the list"""

names = ['Janek', 'Inga', 'Krzysiek', 'Basia']
ladies = []
for name in names:
    if name[-1] == 'a':
        ladies.append(name)

print(ladies)

ladies = [name for name in names if name[-1] == 'a']
print(ladies)

"""filtering the list and operation on selected elements"""

persons = [
    ('Jack', 'Smith', 'New York'),
    ('Fill', 'Taylor', 'Chicago'),
    ('Thomas', 'Johnson', 'Los Angeles')
]

persons_g = [person for person in persons if person[-1][0] == 'N']
print(persons_g)

persons_upp = [(person[0], person[1], person[2].upper()) for person in persons_g]
# parentheses () say this is supposed to be a tuple
print(persons_upp)

# combination of two comprehension lists
persons_2_in_1 = [(p[0], p[1], p[2].upper()) for p in persons if p[-1][0] == 'N']

print(persons_2_in_1)
