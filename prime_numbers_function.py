def is_prime(number):
    number = int(number)
    if number in [0, 1]:
        return False

    for div in range(2, int(number ** 0.5 + 1)):
        if number % div == 0:
            return False
    return True


print(is_prime(input('Check that the integer is prime: ')))

