pesel = list(input('Check PESEL: '))
check = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]

control = 0
for pesel_digit, check_digit in zip(pesel, check):
    control += int(pesel_digit) * int(check_digit)

if str(control)[-1] == '0':
    print('CORRECT')
else:
    print('INCORRECT')
