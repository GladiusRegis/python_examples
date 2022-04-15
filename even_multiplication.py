done = False
summary = 1
while not done:
    number = input('Enter a number or enter [exit]: ')
    if number == 'exit':
        done = True
    else:
        number = int(number)
        if number % 2 == 0:
            summary *= number

print(summary)
