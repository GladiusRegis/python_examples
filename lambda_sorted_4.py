names = ['Leon', 'Barbara', 'Czesław', 'Fryderyk']

by_alphabet = sorted(names)
by_last_letter = sorted(names, key=lambda x: x[-1])
by_length = sorted(names, key=len)
by_length_reverse = sorted(names, key=len, reverse=True)

print(by_alphabet)
print(by_last_letter)
print(by_length)
print(by_length_reverse)

print(sorted([1, 2, 3, 0], reverse=True))
print(list(reversed(sorted([1, 2, 3, 0]))))


