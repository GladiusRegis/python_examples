menu = input('Binary value [1], decimal value [2]:')

if menu not in ['1', '2']:
    print("I don't understand, try again")
    quit()

if menu == '1':
    binary = tuple(reversed(input('Enter the binary value: ')))

    length = len(binary)
    totality = 0

    for index in range(0, length):
        number = int(binary[index]) * 2 ** index
        totality += number
    print(totality)


else:
    decimal = int(input('Enter the value in decimal: '))
    decimal_list = []

    while decimal != 0:
        rest_division = decimal % 2
        # print(decimal)
        decimal = decimal//2

        decimal_list.append(rest_division)
        # print(decimal_list)

    totality_binary = list(reversed(decimal_list))
    a = [str(i) for i in totality_binary]
    b = int("".join(a))
    print(b)

