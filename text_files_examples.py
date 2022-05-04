handler = open('test.txt')
line = handler.readline()
print(line)
handler.close()

with open('test.txt') as handler:
    line = handler.readline()
    print(line)


def open(file, mode='r', buffering=None, encoding=None):
    pass


with open('test.txt', 'r') as handler:
    for line in handler:
        print(line.strip())

with open('test.txt', 'r') as handler:
    lines = handler.readlines()
    print(lines)

with open('test.txt', 'w') as handler:
    handler.write('Ala ma kota\n')


with open('test.txt', 'a') as handler:
    handler.write('Ala\n')
with open('test.txt', 'a') as handler:
    handler.write('ma\n')
with open('test.txt', 'a') as handler:
    handler.write('kota\n')

with open('test.txt', 'w') as handler:
    handler.writeline('Ala ma kota')
    