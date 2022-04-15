def get_factorial(number: int = 2) -> int:
    i = number
    factorial = number
    while i > 1:
        number -= 1
        factorial *= number
        i -= 1

    return factorial


value = int(input('Enter a number to calculate the factorial n! : '))
print(get_factorial(value))
