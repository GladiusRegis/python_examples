done = False
number_list = []
summary = 1
while not done:
    number = input('Enter a number or enter [exit]: ')
    if number == 'exit':
        done = True
    else:
        number = int(number)
        if number % 2 == 0:
            number_list.append(number)
length = len(number_list)
for i in range(0, length):
    summary *= number_list[i]
print(summary)
