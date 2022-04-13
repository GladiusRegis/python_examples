def is_prime(number):
    number = int(number)
    if number in [0, 1]:
        return False

    for div in range(2, int(number ** 0.5 + 1)):
        if number % div == 0:
            return False
    return number

# print(is_prime(input('Check that the integer is prime: ')))


def generate_prime_numbers():
    number = 0
    while True:
        if is_prime(number):
            yield number
        number += 1


number_char = int(input('Up to how many digits in a number to count: '))
primes = generate_prime_numbers()

for n in primes:
    print(f'{n} is a prime number')
    if len(str(n)) >= number_char:
        print(f'Generate for {n} numbers')
        primes.close()
