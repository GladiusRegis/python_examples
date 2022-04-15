value = input('Enter a number or enter [exit]: ')
summary = 1
while value != 'exit':
    number = int(value)

    if number % 2 == 0:
        summary *= number

    value = input('Enter a number or enter [exit]: ')

print(f'Product of even values is {summary}')
