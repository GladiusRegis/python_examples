done = False
summary = 1
while not done:
    value = input('Enter a number or enter [exit]: ')
    if value == 'exit':
        done = True
        continue

    number = int(value)

    if number % 2 == 0:
        summary *= number

print(f'Product of even values is {summary}')