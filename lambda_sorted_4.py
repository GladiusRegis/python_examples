names = ['Leon', 'Barbara', 'Czesław', 'Fryderyk']

by_alphabet = sorted(names)
by_last_letter = sorted(names, key=lambda x: x[-1])
by_length = sorted(names, key=len)

print(by_alphabet)
print(by_last_letter)
print(by_length)
