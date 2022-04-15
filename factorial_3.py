def get_factorial(number: int) -> int:
    factorial = 1
    while number > 0:
        factorial *= number
        number -= 1

    return factorial


value = int(input('Enter a number to calculate the factorial n! : '))
print(get_factorial(value))